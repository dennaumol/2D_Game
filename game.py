
from entities import *
from location import *
from interface import *
import random

pygame.init()

true_scroll = [0, 0]


def update_scroll():
    global true_scroll, scroll


def calculate_player_chunk():
    global player
    chunk_col = player.rect.centerx // CHUNK_WIDTH
    chunk_row = player.rect.centery // CHUNK_HEIGHT
    return chunk_col, chunk_row


def sort_objects_by_z_index(objects):
    objects.sort(key=lambda x: x.z_index)
    return objects.copy()


def add_object_to_chunk(object):
    global location
    global nearby_objects
    global nearby_entities
    chunk_col = object.rect.x // CHUNK_WIDTH
    chunk_row = object.rect.y // CHUNK_HEIGHT
    if object.type == ENTITY:
        location.chunks[(chunk_col, chunk_row)].objects[2].append(object)
        return
    location.chunks[(chunk_col, chunk_row)].objects[1].append(object)

def get_objects_around_player():
    global nearby_objects
    global objects_with_collision
    global other_objects
    global projectiles
    global nearby_entities

    nearby_objects.clear()
    objects_with_collision.clear()
    other_objects.clear()
    nearby_entities.clear()

    chunk_col, chunk_row = calculate_player_chunk()
    add_to_objects_with_collision, add_to_other_objects, add_to_entities = location.get_chunk_objects(chunk_col, chunk_row)
    objects_with_collision.extend(add_to_objects_with_collision.copy())
    other_objects.extend(add_to_other_objects.copy())
    nearby_entities.extend(add_to_entities.copy())

    add_to_objects_with_collision, add_to_other_objects, add_to_entities = location.get_chunk_objects(chunk_col - 1, chunk_row)
    objects_with_collision.extend(add_to_objects_with_collision.copy())
    other_objects.extend(add_to_other_objects.copy())
    nearby_entities.extend(add_to_entities.copy())

    add_to_objects_with_collision, add_to_other_objects, add_to_entities = location.get_chunk_objects(chunk_col + 1, chunk_row)
    objects_with_collision.extend(add_to_objects_with_collision.copy())
    other_objects.extend(add_to_other_objects.copy())
    nearby_entities.extend(add_to_entities.copy())

    add_to_objects_with_collision, add_to_other_objects, add_to_entities = location.get_chunk_objects(chunk_col, chunk_row - 1)
    objects_with_collision.extend(add_to_objects_with_collision.copy())
    other_objects.extend(add_to_other_objects.copy())
    nearby_entities.extend(add_to_entities.copy())

    add_to_objects_with_collision, add_to_other_objects, add_to_entities = location.get_chunk_objects(chunk_col, chunk_row + 1)
    objects_with_collision.extend(add_to_objects_with_collision.copy())
    other_objects.extend(add_to_other_objects.copy())
    nearby_entities.extend(add_to_entities.copy())

    add_to_objects_with_collision, add_to_other_objects, add_to_entities = location.get_chunk_objects(chunk_col - 1, chunk_row - 1)
    objects_with_collision.extend(add_to_objects_with_collision.copy())
    other_objects.extend(add_to_other_objects.copy())
    nearby_entities.extend(add_to_entities.copy())

    add_to_objects_with_collision, add_to_other_objects, add_to_entities = location.get_chunk_objects(chunk_col + 1, chunk_row - 1)
    objects_with_collision.extend(add_to_objects_with_collision.copy())
    other_objects.extend(add_to_other_objects.copy())
    nearby_entities.extend(add_to_entities.copy())

    add_to_objects_with_collision, add_to_other_objects, add_to_entities = location.get_chunk_objects(chunk_col - 1, chunk_row + 1)
    objects_with_collision.extend(add_to_objects_with_collision.copy())
    other_objects.extend(add_to_other_objects.copy())
    nearby_entities.extend(add_to_entities.copy())

    add_to_objects_with_collision, add_to_other_objects, add_to_entities = location.get_chunk_objects(chunk_col + 1, chunk_row + 1)
    objects_with_collision.extend(add_to_objects_with_collision.copy())
    other_objects.extend(add_to_other_objects.copy())
    nearby_entities.extend(add_to_entities.copy())

    nearby_objects.extend(other_objects.copy())
    nearby_objects.extend(nearby_entities.copy())
    nearby_objects.extend(objects_with_collision.copy())
    nearby_objects = sort_objects_by_z_index(nearby_objects)


def calculate_object_chunk(object):
    chunk_col = object.rect.x // CHUNK_WIDTH
    chunk_row = object.rect.y // CHUNK_HEIGHT
    return chunk_col, chunk_row




clock = pygame.time.Clock()
location = YellowDesert()
location.generate()
player = Player(*location.player_spawn)

all_entities = []
all_entities.extend(location.enemies)


nearby_objects = []
objects_with_collision = []
nearby_entities = []
other_objects = []
dead = []

true_scroll[0] += (player.rect.x - true_scroll[0] - (SCREEN_WIDTH // 2 - player.rect.width // 2))
true_scroll[1] += (player.rect.y - true_scroll[1] - (SCREEN_HEIGHT - player.rect.height // 2))


update_chunks_tick = 30
current_update_chunks_tick = update_chunks_tick

add_object_to_chunk(player)

main_game_loop = True

healthbar = HeathBar()



while main_game_loop:
    

    dead = []
    get_objects_around_player()
    true_scroll[0] += (player.rect.x - true_scroll[0] - (SCREEN_WIDTH / 2 - player.rect.width / 2)) / 15
    true_scroll[1] += (player.rect.y - true_scroll[1] - (SCREEN_HEIGHT - player.rect.height * 3)) / 15

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
        add_object_to_chunk(projectile)
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

    healthbar.update(player)
    healthbar.draw(SCREEN)

    for object in nearby_objects:
        if object.name != LEVEL_OBJECT:
            chunk_col, chunk_row = calculate_object_chunk(object)
            if object.type == ENTITY:
                location.chunks[(chunk_col, chunk_row)].objects[2].remove(object)
            elif object not in objects_with_collision:
                location.chunks[(chunk_col, chunk_row)].objects[1].remove(object)
            else:
                location.chunks[(chunk_col, chunk_row)].objects[0].remove(object)
        if object.name == SPARK:
            object.update()
            if not spark.alive:
                dead.append(spark)
        if object.name == EXPLOSION:
            object.update(entities=nearby_entities + [player])
            if object.end:
                dead.append(object)
        if object.type == ENTITY:

            if object.name == SMALL_MONSTER:
                if (object.self_destroy_cur_count_down <= 0 and object.self_destroy) or object.hp <= 0:
                    explosion = Explosion(object.rect.centerx, object.rect.top)
                    add_object_to_chunk(explosion)
                    dead.append(object)
            elif object.hp <= 0:
                dead.append(object)

            object.update(scroll=scroll, objects_with_collision=objects_with_collision, player=player,
                          y_dead_bottom=location.dead_bottom)
        if object.name == PROJECTILE:
            object.update(objects_with_collision=objects_with_collision, entities=nearby_entities)
            if object.collide:
                dead.append(object)
                for _ in range(10):
                    spark = Spark(list(object.rect.center), math.radians(random.randint(0, 360)), random.randint(3, 6), (255, 255, 255), 2)
                    add_object_to_chunk(spark)
        if object.name != LEVEL_OBJECT:
            chunk_col, chunk_row = calculate_object_chunk(object)
            if object.type == ENTITY:
                location.chunks[(chunk_col, chunk_row)].objects[2].append(object)
            elif object not in objects_with_collision:
                location.chunks[(chunk_col, chunk_row)].objects[1].append(object)
            else:
                location.chunks[(chunk_col, chunk_row)].objects[0].append(object)
        object.draw(SCREEN, scroll)
    for object in dead:
        chunk_col, chunk_row = calculate_object_chunk(object)
        if object.type == ENTITY:
            location.chunks[(chunk_col, chunk_row)].objects[2].remove(object)
        elif object not in objects_with_collision:
            print(object.name)
            location.chunks[(chunk_col, chunk_row)].objects[1].remove(object)
        else:
            location.chunks[(chunk_col, chunk_row)].objects[0].remove(object)
    dead.clear()

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()