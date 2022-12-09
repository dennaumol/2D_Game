import pygame
from entities import *
from settings import *
from location import *

pygame.init()

true_scroll = [0, 0]


player = Player(0, -500)
clock = pygame.time.Clock()


location = YellowDesert(0, 0)
objects_with_collision, front, behind = location.generate()
all_objects = []

enemies = location.enemies


all_objects.extend(behind)
all_objects.extend(objects_with_collision)
all_objects.append(player)
all_objects.extend(enemies)
all_objects.extend(front)
existing_entities = []

main_game_loop = True
while main_game_loop:

    if player.hp > 0 and len(existing_entities) < 3:
        all_objects.append(SmallMonster(player.rect.x + randint(-1000, 1000), player.rect.y - 350))



    true_scroll[0] += (player.rect.x - true_scroll[0] - (SCREEN_WIDTH // 2 - player.rect.width // 2)) / 10
    true_scroll[1] += (player.rect.y - true_scroll[1] - (SCREEN_HEIGHT // 2 - player.rect.height // 2)) / 10
    true_scroll[1] = min(location.bottom - (SCREEN_HEIGHT + player.rect.height), true_scroll[1])

    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                player.jump = True
            if event.key == pygame.K_q:
                player.dash = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.shooting = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            player.shooting = False

    if player.shooting and player.shooting_tick_cur <= 0:
        projectile = player.shot(scroll)
        all_objects.insert(0, projectile)
        player.shooting_tick_cur = player.shooting_tick

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.moving_left = True
        player.is_moving = True
        player.right = False
    if keys[pygame.K_d]:
        player.moving_right = True
        player.is_moving = True
        player.right = True
    if not keys[pygame.K_a]:
        player.moving_left = False
    if not keys[pygame.K_d]:
        player.moving_right = False
    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        player.is_moving = False
    SCREEN.fill((247, 101, 101))
    location.background.draw(SCREEN)

    for object in all_objects:
        if abs(abs(player.rect.centerx + scroll[0]) - abs(object.rect.centerx + scroll[0])) >= SCREEN_WIDTH // 0.5:
            if object.type == ENTITY:
                all_objects.remove(object)
                if object in existing_entities:
                    existing_entities.remove(object)
            continue
        if object.name == EXPLOSION:
            object.update(entities=existing_entities)
            if object.end:
                all_objects.remove(object)
        if object.type == ENTITY:
            if object.rect.y > location.bottom or object.hp <= 0:
                all_objects.remove(object)
                existing_entities.remove(object)

                continue
            if object.rect.y <= location.bottom and object.hp > 0:
                if object not in existing_entities:
                    existing_entities.append(object)
            if object.name == SMALL_MONSTER:
                if object.self_destroy_cur_count_down < 0:
                    all_objects.append(Explosion(object.rect.centerx, object.rect.centery))
                    all_objects.remove(object)
                    existing_entities.remove(object)
            object.update(scroll=scroll, objects_with_collision=objects_with_collision, player=player,
                          y_dead_bottom=location.bottom)
        if object.name == PROJECTILE:
            object.update(objects_with_collision=objects_with_collision, entities=existing_entities)
            if object.collide:
                all_objects.remove(object)
        object.draw(SCREEN, scroll)


    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()