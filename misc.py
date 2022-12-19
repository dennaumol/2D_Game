from images import *
import random
import math

class Explosion:
    def __init__(self, x, y):
        self.z_index = 100
        self.tick = 0
        self.type = MISC
        self.images = explosion_2_images
        self.image = self.images[0]
        self.rect = self.images[6].get_bounding_rect()
        self.rect.center = (x, y)
        self.damage_rect = self.rect
        self.damage_rect.width *= 1
        self.damage_rect.height *= 1
        self.damage_rect.center = self.rect.center
        self.damage = False
        self.name = EXPLOSION
        self.end = False

    def update(self, *args, **kwargs):
        self.image = self.images[self.tick // 6]
        self.tick += 1
        if self.tick >= 61:
            self.end = True
            self.tick = 0
        entities = kwargs['entities']

        if not self.damage:
            self.damage = True
            for entity in entities:
                if entity.rect.colliderect(self.damage_rect):
                    entity.take_damage(1000)

    def draw(self, surface, scroll):
        image_rect = self.image.get_rect(centerx=self.rect.centerx - scroll[0], bottom=self.rect.bottom - scroll[1])
        #pygame.draw.rect(surface, "red", (self.damage_rect.x - scroll[0], self.damage_rect.y - scroll[1], self.damage_rect.width, self.damage_rect.height))
        surface.blit(self.image, image_rect)


class Spark:
    def __init__(self, loc, angle, speed, color, scale=1):
        self.loc = loc
        self.angle = angle
        self.speed = speed
        self.scale = scale
        self.color = color
        self.alive = True
        self.type = MISC
        self.z_index = 99
        self.name = SPARK
        self.type = MISC
        self.rect = pygame.Rect(self.loc[0], self.loc[1], 1, 1)

    def point_towards(self, angle, rate):
        rotate_direction = ((angle - self.angle + math.pi * 3) % (math.pi * 2)) - math.pi
        try:
            rotate_sign = abs(rotate_direction) / rotate_direction
        except ZeroDivisionError:
            rotate_sing = 1
        if abs(rotate_direction) < rate:
            self.angle = angle
        else:
            self.angle += rate * rotate_sign

    def calculate_movement(self, dt):
        return [math.cos(self.angle) * self.speed * dt, math.sin(self.angle) * self.speed * dt]


    # gravity and friction
    def velocity_adjust(self, friction, force, terminal_velocity, dt):
        movement = self.calculate_movement(dt)
        movement[1] = min(terminal_velocity, movement[1] + force * dt)
        movement[0] *= friction
        self.angle = math.atan2(movement[1], movement[0])
        # if you want to get more realistic, the speed should be adjusted here

    def move(self, dt):
        movement = self.calculate_movement(dt)
        self.loc[0] += movement[0]
        self.loc[1] += movement[1]
        
    
    

        # a bunch of options to mess around with relating to angles...
        self.point_towards(math.pi / 2, 0.02)
        #self.velocity_adjust(0.975, 0.2, 8, dt)
        #self.angle += 0.1

        self.speed -= 0.1
        self.rect = pygame.Rect(self.loc[0], self.loc[1], 3, 3)
        if self.speed <= 0:
            self.alive = False

        
    def update(self, *args, **kwargs):
        self.move(1)

    def draw(self, surface, scroll):
        if self.alive:
            points = [
                [self.loc[0] + math.cos(self.angle) * self.speed * self.scale - scroll[0], self.loc[1] + math.sin(self.angle) * self.speed * self.scale - scroll[1]],
                [self.loc[0] + math.cos(self.angle + math.pi / 2) * self.speed * self.scale * 0.3 - scroll[0], self.loc[1] + math.sin(self.angle + math.pi / 2) * self.speed * self.scale * 0.3 - scroll[1]],
                [self.loc[0] - math.cos(self.angle) * self.speed * self.scale * 3.5 - scroll[0], self.loc[1] - math.sin(self.angle) * self.speed * self.scale * 3.5 - scroll[1]],
                [self.loc[0] + math.cos(self.angle - math.pi / 2) * self.speed * self.scale * 0.3 - scroll[0], self.loc[1] - math.sin(self.angle + math.pi / 2) * self.speed * self.scale * 0.3 - scroll[1]],
                ]
            pygame.draw.polygon(surface, self.color, points)











