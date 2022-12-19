import pygame
pygame.mixer.init()

FPS = 60
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
GRAVITY = 0.75
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
CHUNK_SIZE = CHUNK_WIDTH, CHUNK_HEIGHT = 1000, 1000
ENTITY = 'entity'
LEVEL_OBJECT = 'level object'
MISC = 'misc'
PLAYER = 'player'
EXPLOSIVE = 'explosive'
EXPLOSION = 'explosion'
BORDER = 'border'
PROJECTILE = 'projectile'
SPARK = 'SPARK'
FLYING_IRON_THING = 'flying iron thing'