from sounds import *
from misc import *
from random import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, z_index=0):
        super(Entity, self).__init__()
        self.death_animation_length_sec = FPS * 3
        self.current_death_animation_tick = self.death_animation_length_sec
        self.left = False
        self.moving_left = False
        self.moving_right = False
        self.right = True
        self.is_moving = False
        self.animation_tick = 0
        self.ang = 90
        self.platform = False
        self.type = ENTITY
        self.hp = 100
        self.max_hp = 100
        self.dx = 0
        self.dy = 0
        self.z_index = z_index
        self.alive = True
        self.can_be_deleted = True
        self.can_be_deleted = False
        self.death_punch_y = False
        self.death_punch_x = False

    def draw(self, surface, scroll):
        image_rect = self.image.get_rect(centerx=self.rect.centerx - scroll[0], bottom=self.rect.bottom - scroll[1])
        # pygame.draw.rect(surface, "red", (self.rect.x - scroll[0], self.rect.y - scroll[1], self.rect.width, self.rect.height))
        surface.blit(self.image, image_rect)

    def check_collisions(self, objects_with_collision):
        for object in objects_with_collision:
            if object.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.rect.width,
                                       self.rect.height) and not object.platform:
                self.dx = 0
            # check for collision in the y direction
            if object.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0 and not object.platform:
                    self.vel_y = 0
                    self.dy = object.rect.bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0 and not object.platform:
                    self.vel_y = 0
                    self.in_air = False
                    self.before_fall_x, self.before_fall_y = self.rect.center
                    self.dy = object.rect.top - self.rect.bottom
                    if self.hp <= 0:
                        self.death_punch_x = True
                elif self.vel_y >= 0 and object.platform and not (self.rect.bottom > object.rect.top):
                    self.vel_y = 0
                    self.in_air = False
                    self.before_fall_x, self.before_fall_y = self.rect.center
                    self.dy = object.rect.top - self.rect.bottom

    def take_damage(self, damage):
        self.hp -= damage


class Player(Entity):
    def __init__(self, x, y, z_index=0):
        super(Player, self).__init__(z_index)
        self.image = player_idle_90_ah
        self.rect = self.image.get_bounding_rect()
        self.rect.width //= 3
        self.rect.center = (x, y)
        self.shooting = False
        self.speed = 11
        self.shooting_tick = 21
        self.shooting_tick_cur = 0
        self.dash = False
        self.dash_speed = 200
        self.jump = False
        self.vel_y = 0
        self.in_air = False
        self.dash_cur_cooldown = 0
        self.dash_max_count = 2
        self.dash_cur_count = 1
        self.dash_cooldown_sec = 2
        self.extra_jumps = 1
        self.extra_cur_jumps = 1
        self.before_fall_x, self.before_fall_y = self.rect.center
        self.hp = 500
        self.max_hp = 500
        self.name = PLAYER

    def shot(self, scroll):
        mx, my = pygame.mouse.get_pos()
        start_pos = (self.rect.centerx, self.rect.top + 34)
        rot = math.atan2(my + scroll[1] - start_pos[1], mx + scroll[0] - start_pos[0])
        move = math.cos(rot) * 20, math.sin(rot) * 20
        projectile = Projectile(start_pos[0], start_pos[1], 45, -rot, move, -100)
        shot_sound_0.play()

        return projectile

    def play_death_animation(self):
        if not self.can_be_deleted:
            if not self.death_punch_x:
                self.dx -= 3
            if not self.death_punch_y:
                self.vel_y = - 19
                self.death_punch_y = True
            self.current_death_animation_tick -= 1
            print(self.current_death_animation_tick)
            if self.current_death_animation_tick <= 0:
                self.can_be_deleted = True

    def update(self, *args, **kwargs):
        self.shooting_tick_cur -= 1
        mouse_x, mouse_y = pygame.mouse.get_pos()
        super(Player, self).update(*args, **kwargs)
        self.dx = 0
        self.dy = 0

        if self.hp <= 0:
            self.play_death_animation()

        self.dash_cur_cooldown -= 1
        if self.dash_cur_count == self.dash_max_count:
            self.dash_cur_cooldown = FPS * self.dash_cooldown_sec
        if self.dash_cur_cooldown <= 0:
            self.dash_cur_cooldown = FPS * self.dash_cooldown_sec
            self.dash_cur_count += 1

        objects_with_collision = kwargs['objects_with_collision']
        scroll = kwargs['scroll']
        y_dead_bottom = kwargs['y_dead_bottom']

        if self.hp > 0:
            if self.rect.bottom > y_dead_bottom:
                self.take_damage(self.hp // 4 + 15)
                self.rect.center = self.before_fall_x, self.before_fall_y

        if not self.in_air:
            self.extra_cur_jumps = self.extra_jumps

        if self.jump and not self.in_air and self.hp > 0:
            self.vel_y = -14
            self.jump = False
            self.in_air = True

        if self.hp > 0:
            if self.moving_left:
                self.dx = -self.speed

            if self.moving_right:
                self.dx = self.speed

        if self.dash and self.dash_cur_count > 0 and self.hp > 0:
            if self.moving_right:
                self.dx = self.dash_speed
            elif self.moving_left:
                self.dx = -self.dash_speed

            if not self.is_moving:
                if mouse_x + scroll[0] >= self.rect.centerx:
                    self.dx = self.dash_speed
                else:
                    self.dx = -self.dash_speed
            self.dash_cur_count -= 1

        if self.extra_cur_jumps > 0 and self.in_air and self.jump and self.hp > 0:
            self.vel_y = -14
            self.extra_cur_jumps -= 1
            self.jump = False
        if self.dash:
            self.dash = False

        if self.in_air:
            self.jump = False

        self.vel_y += GRAVITY
        self.dy += self.vel_y

        self.check_collisions(objects_with_collision)

        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.dx == 0:
            self.is_moving = False

        start_pos = (self.rect.centerx + self.rect.width // 2,
                     self.rect.top + self.rect.height // 2)
        ang = math.atan2(mouse_x + scroll[0] - start_pos[0], mouse_y + scroll[1] - start_pos[1])
        self.ang = abs(math.degrees(ang))

        self.image = player_idle_90_ah

        if (self.right and mouse_x + scroll[0] >= self.rect.centerx) or (
                not self.right and mouse_x + scroll[0] < self.rect.centerx):

            if self.is_moving:
                self.image = player_run_90_ah[self.animation_tick // 20]
                if 0 <= self.ang < 13:
                    self.image = player_run_6_ah[self.animation_tick // 20]
                elif 13 <= self.ang < 20:
                    self.image = player_run_13_ah[self.animation_tick // 20]
                elif 20 <= self.ang < 27:
                    self.image = player_run_20_ah[self.animation_tick // 20]
                elif 27 <= self.ang < 34:
                    self.image = player_run_27_ah[self.animation_tick // 20]
                elif 34 <= self.ang < 41:
                    self.image = player_run_34_ah[self.animation_tick // 20]
                elif 41 <= self.ang < 48:
                    self.image = player_run_41_ah[self.animation_tick // 20]
                elif 48 <= self.ang < 55:
                    self.image = player_run_48_ah[self.animation_tick // 20]
                elif 55 <= self.ang < 62:
                    self.image = player_run_55_ah[self.animation_tick // 20]
                elif 62 <= self.ang < 69:
                    self.image = player_run_62_ah[self.animation_tick // 20]
                elif 69 <= self.ang < 76:
                    self.image = player_run_69_ah[self.animation_tick // 20]
                elif 76 <= self.ang < 83:
                    self.image = player_run_76_ah[self.animation_tick // 20]
                elif 83 <= self.ang < 90:
                    self.image = player_run_83_ah[self.animation_tick // 20]
                elif 90 <= self.ang < 97:
                    self.image = player_run_90_ah[self.animation_tick // 20]
                elif 97 <= self.ang < 105:
                    self.image = player_run_97_ah[self.animation_tick // 20]
                elif 105 <= self.ang < 112:
                    self.image = player_run_105_ah[self.animation_tick // 20]
                elif 112 <= self.ang < 119:
                    self.image = player_run_112_ah[self.animation_tick // 20]
                elif 119 <= self.ang < 126:
                    self.image = player_run_119_ah[self.animation_tick // 20]
                elif 126 <= self.ang < 133:
                    self.image = player_run_126_ah[self.animation_tick // 20]
                elif 133 <= self.ang < 140:
                    self.image = player_run_133_ah[self.animation_tick // 20]
                elif 140 <= self.ang < 147:
                    self.image = player_run_140_ah[self.animation_tick // 20]
                elif 147 <= self.ang < 154:
                    self.image = player_run_147_ah[self.animation_tick // 20]
                elif 154 <= self.ang < 161:
                    self.image = player_run_154_ah[self.animation_tick // 20]
                elif 161 <= self.ang < 168:
                    self.image = player_run_161_ah[self.animation_tick // 20]
                elif 168 <= self.ang < 175:
                    self.image = player_run_168_ah[self.animation_tick // 20]
                elif 175 <= self.ang <= 180:
                    self.image = player_run_175_ah[self.animation_tick // 20]

            if not self.is_moving:
                if 0 <= self.ang < 13:
                    self.image = player_idle_6_ah
                elif 13 <= self.ang < 20:
                    self.image = player_idle_13_ah
                elif 20 <= self.ang < 27:
                    self.image = player_idle_20_ah
                elif 27 <= self.ang < 34:
                    self.image = player_idle_27_ah
                elif 34 <= self.ang < 41:
                    self.image = player_idle_34_ah
                elif 41 <= self.ang < 48:
                    self.image = player_idle_41_ah
                elif 48 <= self.ang < 55:
                    self.image = player_idle_48_ah
                elif 55 <= self.ang < 62:
                    self.image = player_idle_55_ah
                elif 62 <= self.ang < 69:
                    self.image = player_idle_62_ah
                elif 69 <= self.ang < 76:
                    self.image = player_idle_69_ah
                elif 76 <= self.ang < 83:
                    self.image = player_idle_76_ah
                elif 83 <= self.ang < 90:
                    self.image = player_idle_83_ah
                elif 90 <= self.ang < 97:
                    self.image = player_idle_90_ah
                elif 97 <= self.ang < 105:
                    self.image = player_idle_97_ah
                elif 105 <= self.ang < 112:
                    self.image = player_idle_105_ah
                elif 112 <= self.ang < 119:
                    self.image = player_idle_112_ah
                elif 119 <= self.ang < 126:
                    self.image = player_idle_119_ah
                elif 126 <= self.ang < 133:
                    self.image = player_idle_126_ah
                elif 133 <= self.ang < 140:
                    self.image = player_idle_133_ah
                elif 140 <= self.ang < 147:
                    self.image = player_idle_140_ah
                elif 147 <= self.ang < 154:
                    self.image = player_idle_147_ah
                elif 154 <= self.ang < 161:
                    self.image = player_idle_154_ah
                elif 161 <= self.ang < 168:
                    self.image = player_idle_161_ah
                elif 168 <= self.ang < 175:
                    self.image = player_idle_168_ah
                elif 175 <= self.ang <= 180:
                    self.image = player_idle_175_ah

        if (self.right and mouse_x + scroll[0] <= self.rect.centerx) or (
                not self.right and mouse_x + scroll[0] > self.rect.centerx):
            if self.is_moving:
                if 0 <= self.ang < 20:
                    self.image = player_run_13_bk[self.animation_tick // 20]

                elif 20 <= self.ang < 27:
                    self.image = player_run_20_bk[self.animation_tick // 20]

                elif 27 <= self.ang < 34:
                    self.image = player_run_27_bk[self.animation_tick // 20]

                elif 34 <= self.ang < 41:
                    self.image = player_run_34_bk[self.animation_tick // 20]

                elif 41 <= self.ang < 48:
                    self.image = player_run_41_bk[self.animation_tick // 20]

                elif 48 <= self.ang < 55:
                    self.image = player_run_48_bk[self.animation_tick // 20]

                elif 55 <= self.ang < 62:
                    self.image = player_run_55_bk[self.animation_tick // 20]

                elif 62 <= self.ang < 69:
                    self.image = player_run_62_bk[self.animation_tick // 20]

                elif 69 <= self.ang < 76:
                    self.image = player_run_69_bk[self.animation_tick // 20]

                elif 76 <= self.ang < 83:
                    self.image = player_run_76_bk[self.animation_tick // 20]

                elif 83 <= self.ang < 90:
                    self.image = player_run_83_bk[self.animation_tick // 20]

                elif 90 <= self.ang < 97:
                    self.image = player_run_90_bk[self.animation_tick // 20]

                elif 97 <= self.ang < 105:
                    self.image = player_run_97_bk[self.animation_tick // 20]

                elif 105 <= self.ang < 112:
                    self.image = player_run_105_bk[self.animation_tick // 20]

                elif 112 <= self.ang < 119:
                    self.image = player_run_112_bk[self.animation_tick // 20]

                elif 119 <= self.ang < 126:
                    self.image = player_run_119_bk[self.animation_tick // 20]

                elif 126 <= self.ang < 133:
                    self.image = player_run_126_bk[self.animation_tick // 20]

                elif 133 <= self.ang < 140:
                    self.image = player_run_133_bk[self.animation_tick // 20]

                elif 140 <= self.ang < 147:
                    self.image = player_run_140_bk[self.animation_tick // 20]

                elif 147 <= self.ang < 154:
                    self.image = player_run_147_bk[self.animation_tick // 20]

                elif 154 <= self.ang < 161:
                    self.image = player_run_154_bk[self.animation_tick // 20]

                elif 161 <= self.ang < 168:
                    self.image = player_run_161_bk[self.animation_tick // 20]

                elif 168 <= self.ang < 175:
                    self.image = player_run_168_bk[self.animation_tick // 20]

                elif 175 <= self.ang < 180:
                    self.image = player_run_175_bk[self.animation_tick // 20]

            if not self.is_moving:
                if 0 <= self.ang < 6:
                    self.image = player_idle_13_bk

                elif 6 <= self.ang < 20:
                    self.image = player_idle_13_bk

                elif 20 <= self.ang < 27:
                    self.image = player_idle_20_bk

                elif 27 <= self.ang < 34:
                    self.image = player_idle_27_bk

                elif 34 <= self.ang < 41:
                    self.image = player_idle_34_bk

                elif 41 <= self.ang < 48:
                    self.image = player_idle_41_bk

                elif 48 <= self.ang < 55:
                    self.image = player_idle_48_bk

                elif 55 <= self.ang < 62:
                    self.image = player_idle_55_bk

                elif 62 <= self.ang < 69:
                    self.image = player_idle_62_bk

                elif 69 <= self.ang < 76:
                    self.image = player_idle_69_bk

                elif 76 <= self.ang < 83:
                    self.image = player_idle_76_bk

                elif 83 <= self.ang < 90:
                    self.image = player_idle_83_bk

                elif 90 <= self.ang < 97:
                    self.image = player_idle_90_bk

                elif 97 <= self.ang < 105:
                    self.image = player_idle_97_bk

                elif 105 <= self.ang < 112:
                    self.image = player_idle_105_bk

                elif 112 <= self.ang < 119:
                    self.image = player_idle_112_bk

                elif 119 <= self.ang < 126:
                    self.image = player_idle_119_bk

                elif 126 <= self.ang < 133:
                    self.image = player_idle_126_bk

                elif 133 <= self.ang < 140:
                    self.image = player_idle_133_bk

                elif 140 <= self.ang < 147:
                    self.image = player_idle_140_bk

                elif 147 <= self.ang < 154:
                    self.image = player_idle_147_bk

                elif 154 <= self.ang < 161:
                    self.image = player_idle_154_bk

                elif 161 <= self.ang < 168:
                    self.image = player_idle_161_bk

                elif 168 <= self.ang < 175:
                    self.image = player_idle_168_bk

                elif 175 <= self.ang <= 180:
                    self.image = player_idle_175_bk

        if not self.right:
            self.image = pygame.transform.flip(self.image, True, False)

        self.animation_tick += 2
        if self.animation_tick >= 80:
            self.animation_tick = 0


class Explosive(Player):
    def __init__(self, x, y, hp=200, z_index=0):
        super(Explosive, self).__init__(x, y, z_index)
        self.image = explosive_idle_image
        self.rect = self.image.get_bounding_rect()
        self.rect.center = (x, y)
        self.speed = 4.5
        self.self_destroy = False
        self.self_destroy_count_down_sec = 0.10
        self.self_destroy_cur_count_down = 100
        self.name = EXPLOSIVE
        self.hp = hp
        self.max_hp = hp
        self.jump = False

    def take_damage(self, damage):
        self.hp -= damage

    def update(self, *args, **kwargs):
        self.dx = 0
        self.dy = 0

        objects_with_collision = kwargs['objects_with_collision']
        player = kwargs['player']

        if not self.self_destroy:
            if self.speed <= abs(abs(player.rect.centerx) - abs(self.rect.centerx)) <= 700 and \
                    abs(abs(player.rect.centery) - abs(self.rect.centery)) <= 300:
                if player.rect.centerx > self.rect.centerx:
                    self.dx = self.speed
                    self.right = False

                else:
                    self.dx = -self.speed
                    self.right = True
                if randint(0, 60) == 0:
                    self.jump = True
                if 50 <= abs(abs(player.rect.centery) - abs(self.rect.centery)) <= 300:
                    if player.rect.centery < self.rect.centery and not self.in_air:
                        self.jump = True
                    else:
                        self.jump = False
            if abs(abs(player.rect.centerx) - abs(self.rect.centerx)) <= 30 and \
                    abs(abs(player.rect.centery) - abs(self.rect.centery)) <= 30:
                self.self_destroy = True
                self.self_destroy_cur_count_down = self.self_destroy_count_down_sec * FPS

            if self.jump and not self.in_air:
                self.vel_y = -17
                self.jump = False
                self.in_air = True

        if self.self_destroy:
            self.self_destroy_cur_count_down -= 1

        if self.moving_left:
            self.dx = -self.speed

        if self.moving_right:
            self.dx = self.speed

        if self.dash and self.dash_cur_count > 0:
            if self.moving_right:
                self.dx = self.dash_speed
            elif self.moving_left:
                self.dx = -self.dash_speed

        if self.in_air:
            self.jump = False

        self.vel_y += GRAVITY
        self.dy += self.vel_y

        self.check_collisions(objects_with_collision)

        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.dx != 0:
            self.is_moving = True
        else:
            self.is_moving = False

        if self.is_moving:
            self.image = explosive_walk_images[self.animation_tick // 10]
        if not self.is_moving:
            self.image = explosive_idle_image

        if not self.right:
            self.image = pygame.transform.flip(self.image, True, False)

        self.animation_tick += 3
        if self.animation_tick >= 61:
            self.animation_tick = 0


class Projectile(Entity):
    def __init__(self, x, y, damage, ang, move, z_index=0):
        super(Projectile, self).__init__(z_index)
        self.image, self.rect, = rot_center(blue_projectile, math.degrees(ang), x, y)
        self.move = move
        self.damage = damage
        self.type = PROJECTILE
        self.name = PROJECTILE
        self.collide = False
        self.tick = 0
        self.living_time_sec = 2

    def update(self, *args, **kwargs):
        self.rect.x += self.move[0]
        self.rect.y += self.move[1]
        self.tick += 1

        if self.tick >= self.living_time_sec * FPS:
            self.collide = True
            return

        objects_with_collision = kwargs['objects_with_collision']
        for object in objects_with_collision:
            if object.rect.x <= self.rect.centerx <= object.rect.x + object.rect.width and \
                    object.rect.y <= self.rect.centery <= object.rect.y + object.rect.height:
                self.collide = True
                return

        entities = kwargs['entities']
        for entity in entities:
            if entity.name == PLAYER:
                continue
            if entity.rect.colliderect(self.rect):
                entity.take_damage(self.damage)
                self.collide = True


class FlyingIronThing(Entity):
    def __init__(self, x, y, z_index):
        super(FlyingIronThing, self).__init__(z_index)
        self.name = FLYING_IRON_THING

    def update(self, *args, **kwargs):
        self.dx = 0
        self.dy = 0

        objects_with_collision = kwargs['objects_with_collision']
        player = kwargs['player']

        if not self.self_destroy:
            if self.speed <= abs(abs(player.rect.centerx) - abs(self.rect.centerx)) <= 700 and \
                    abs(abs(player.rect.centery) - abs(self.rect.centery)) <= 300:
                if player.rect.centerx > self.rect.centerx:
                    self.dx = self.speed
                    self.right = False

                else:
                    self.dx = -self.speed
                    self.right = True
                if randint(0, 60) == 0:
                    self.jump = True
                if 50 <= abs(abs(player.rect.centery) - abs(self.rect.centery)) <= 300:
                    if player.rect.centery < self.rect.centery and not self.in_air:
                        self.jump = True
                    else:
                        self.jump = False
            if abs(abs(player.rect.centerx) - abs(self.rect.centerx)) <= 30 and \
                    abs(abs(player.rect.centery) - abs(self.rect.centery)) <= 30:
                self.self_destroy = True
                self.self_destroy_cur_count_down = self.self_destroy_count_down_sec * FPS

            if self.jump and not self.in_air:
                self.vel_y = -17
                self.jump = False
                self.in_air = True

        if self.self_destroy:
            self.self_destroy_cur_count_down -= 1

        if self.moving_left:
            self.dx = -self.speed

        if self.moving_right:
            self.dx = self.speed

        if self.dash and self.dash_cur_count > 0:
            if self.moving_right:
                self.dx = self.dash_speed
            elif self.moving_left:
                self.dx = -self.dash_speed

        if self.in_air:
            self.jump = False

        self.vel_y += GRAVITY
        self.dy += self.vel_y

        self.check_collisions(objects_with_collision)

        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.dx != 0:
            self.is_moving = True
        else:
            self.is_moving = False

        if self.is_moving:
            self.image = explosive_walk_images[self.animation_tick // 10]
        if not self.is_moving:
            self.image = explosive_idle_image

        if not self.right:
            self.image = pygame.transform.flip(self.image, True, False)

        self.animation_tick += 3
        if self.animation_tick >= 61:
            self.animation_tick = 0
