import pygame

TILE_SCALE = 3.5

from settings import *

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_0.png')
yellow_sand_0_image = pygame.transform.scale(image,
                                             (int(image.get_width() * TILE_SCALE),
                                              int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_1.png')
yellow_sand_1_image = pygame.transform.scale(image,
                                             (int(image.get_width() * TILE_SCALE),
                                              int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_2.png')
yellow_sand_2_image = pygame.transform.scale(image,
                                             (int(image.get_width() * TILE_SCALE),
                                              int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_3.png')
yellow_sand_3_image = pygame.transform.scale(image,
                                             (int(image.get_width() * TILE_SCALE),
                                              int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_decoration_1.png')
yellow_sand_decoration_1_image = pygame.transform.scale(image,
                                                        (int(image.get_width() * TILE_SCALE),
                                                         int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_decoration_2.png')
yellow_sand_decoration_2_image = pygame.transform.scale(image,
                                                        (int(image.get_width() * TILE_SCALE),
                                                         int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_decoration_3.png')
yellow_sand_decoration_3_image = pygame.transform.scale(image,
                                                        (int(image.get_width() * TILE_SCALE),
                                                         int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_under_0.png')
yellow_sand_under_0_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_under_1.png')
yellow_sand_under_1_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_under_2.png')
yellow_sand_under_2_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//platforms//gray//flying//single.png')
gray_single_flying_platform_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//platforms//gray//flying//triple_0.png')
gray_triple_flying_platform_0_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//platforms//gray//flying//triple_1.png')
gray_triple_flying_platform_1_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data/images/level_objects/platforms/gray/columns/0.png')
gray_column_0_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data/images/level_objects/platforms/gray/columns_tops/0.png')
gray_column_top_0_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data/images/level_objects/platforms/gray/columns_tops/1.png')
gray_column_top_1_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data/images/level_objects/sand/yellow/sand_block.png')
sand_block_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * TILE_SCALE),
                                                    int(image.get_height() * TILE_SCALE))).convert_alpha(SCREEN)


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Tile, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)

    def draw(self, surface, scroll):
        surface.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))
        # pygame.draw.rect(surface, 'RED',
        # (self.rect.x - scroll[0], self.rect.y - scroll[1], self.rect.width, self.rect.height))







