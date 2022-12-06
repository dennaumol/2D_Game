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

all_objects.extend(behind)
all_objects.extend(objects_with_collision)
all_objects.append(player)
all_objects.extend(front)



main_game_loop = True
while main_game_loop:

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

    player.update(objects_with_collision=objects_with_collision, scroll=scroll, y_dead_bottom=location.bottom)

    for sprite in all_objects:
        sprite.draw(SCREEN, scroll)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()