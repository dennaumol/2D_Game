from settings import *

SCALE = 3


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_0.png')
yellow_sand_0_image = pygame.transform.scale(image,
                                             (int(image.get_width() * SCALE),
                                              int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_1.png')
yellow_sand_1_image = pygame.transform.scale(image,
                                             (int(image.get_width() * SCALE),
                                              int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_2.png')
yellow_sand_2_image = pygame.transform.scale(image,
                                             (int(image.get_width() * SCALE),
                                              int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_3.png')
yellow_sand_3_image = pygame.transform.scale(image,
                                             (int(image.get_width() * SCALE),
                                              int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_decoration_1.png')
yellow_sand_decoration_1_image = pygame.transform.scale(image,
                                                        (int(image.get_width() * SCALE),
                                                         int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_decoration_2.png')
yellow_sand_decoration_2_image = pygame.transform.scale(image,
                                                        (int(image.get_width() * SCALE),
                                                         int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_decoration_3.png')
yellow_sand_decoration_3_image = pygame.transform.scale(image,
                                                        (int(image.get_width() * SCALE),
                                                         int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_under_0.png')
yellow_sand_under_0_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_under_1.png')
yellow_sand_under_1_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//sand//yellow//sand_under_2.png')
yellow_sand_under_2_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//platforms//gray//flying//single.png')
gray_single_flying_platform_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//platforms//gray//flying//triple_0.png')
gray_triple_flying_platform_0_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data//images//level_objects//platforms//gray//flying//triple_1.png')
gray_triple_flying_platform_1_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data/images/level_objects/platforms/gray/columns/0.png')
gray_column_0_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data/images/level_objects/platforms/gray/columns_tops/0.png')
gray_column_top_0_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data/images/level_objects/platforms/gray/columns_tops/1.png')
gray_column_top_1_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

image = pygame.image.load('data/images/level_objects/sand/yellow/sand_block.png')
sand_block_image = pygame.transform.scale(image,
                                                   (int(image.get_width() * SCALE),
                                                    int(image.get_height() * SCALE))).convert_alpha(SCREEN)

from settings import *


player_idle_6_ah = pygame.image.load('data/images/player/ahead/idle/6/0.gif')
player_idle_6_ah = pygame.transform.scale(player_idle_6_ah, (int(player_idle_6_ah.get_width() * SCALE),
                                                         int(player_idle_6_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_13_ah = pygame.image.load('data/images/player/ahead/idle/13/0.gif')
player_idle_13_ah = pygame.transform.scale(player_idle_13_ah, (int(player_idle_13_ah.get_width() * SCALE),
                                                         int(player_idle_13_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_20_ah = pygame.image.load('data/images/player/ahead/idle/20/0.gif')
player_idle_20_ah = pygame.transform.scale(player_idle_20_ah, (int(player_idle_20_ah.get_width() * SCALE),
                                                         int(player_idle_20_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_27_ah = pygame.image.load('data/images/player/ahead/idle/27/0.gif')
player_idle_27_ah = pygame.transform.scale(player_idle_27_ah, (int(player_idle_27_ah.get_width() * SCALE),
                                                         int(player_idle_27_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_34_ah = pygame.image.load('data/images/player/ahead/idle/34/0.gif')
player_idle_34_ah = pygame.transform.scale(player_idle_34_ah, (int(player_idle_34_ah.get_width() * SCALE),
                                                         int(player_idle_34_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_41_ah = pygame.image.load('data/images/player/ahead/idle/41/0.gif')
player_idle_41_ah = pygame.transform.scale(player_idle_41_ah, (int(player_idle_41_ah.get_width() * SCALE),
                                                         int(player_idle_41_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_48_ah = pygame.image.load('data/images/player/ahead/idle/48/0.gif')
player_idle_48_ah = pygame.transform.scale(player_idle_48_ah, (int(player_idle_48_ah.get_width() * SCALE),
                                                         int(player_idle_48_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_55_ah = pygame.image.load('data/images/player/ahead/idle/55/0.gif')
player_idle_55_ah = pygame.transform.scale(player_idle_55_ah, (int(player_idle_55_ah.get_width() * SCALE),
                                                         int(player_idle_55_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_62_ah = pygame.image.load('data/images/player/ahead/idle/62/0.gif')
player_idle_62_ah = pygame.transform.scale(player_idle_62_ah, (int(player_idle_62_ah.get_width() * SCALE),
                                                         int(player_idle_62_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_69_ah = pygame.image.load('data/images/player/ahead/idle/69/0.gif')
player_idle_69_ah = pygame.transform.scale(player_idle_69_ah, (int(player_idle_69_ah.get_width() * SCALE),
                                                         int(player_idle_69_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_76_ah = pygame.image.load('data/images/player/ahead/idle/76/0.gif')
player_idle_76_ah = pygame.transform.scale(player_idle_76_ah, (int(player_idle_76_ah.get_width() * SCALE),
                                                         int(player_idle_76_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_83_ah = pygame.image.load('data/images/player/ahead/idle/83/0.gif')
player_idle_83_ah = pygame.transform.scale(player_idle_83_ah, (int(player_idle_83_ah.get_width() * SCALE),
                                                         int(player_idle_83_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_90_ah = pygame.image.load('data/images/player/ahead/idle/90/0.gif')
player_idle_90_ah = pygame.transform.scale(player_idle_90_ah, (int(player_idle_90_ah.get_width() * SCALE),
                                                         int(player_idle_90_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_97_ah = pygame.image.load('data/images/player/ahead/idle/97/0.gif')
player_idle_97_ah = pygame.transform.scale(player_idle_97_ah, (int(player_idle_97_ah.get_width() * SCALE),
                                                         int(player_idle_97_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_105_ah = pygame.image.load('data/images/player/ahead/idle/105/0.gif')
player_idle_105_ah = pygame.transform.scale(player_idle_105_ah, (int(player_idle_105_ah.get_width() * SCALE),
                                                         int(player_idle_105_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_112_ah = pygame.image.load('data/images/player/ahead/idle/112/0.gif')
player_idle_112_ah = pygame.transform.scale(player_idle_112_ah, (int(player_idle_112_ah.get_width() * SCALE),
                                                         int(player_idle_112_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_119_ah = pygame.image.load('data/images/player/ahead/idle/119/0.gif')
player_idle_119_ah = pygame.transform.scale(player_idle_119_ah, (int(player_idle_119_ah.get_width() * SCALE),
                                                         int(player_idle_119_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_126_ah = pygame.image.load('data/images/player/ahead/idle/126/0.gif')
player_idle_126_ah = pygame.transform.scale(player_idle_126_ah, (int(player_idle_126_ah.get_width() * SCALE),
                                                         int(player_idle_126_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_133_ah = pygame.image.load('data/images/player/ahead/idle/133/0.gif')
player_idle_133_ah = pygame.transform.scale(player_idle_133_ah, (int(player_idle_133_ah.get_width() * SCALE),
                                                         int(player_idle_133_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_140_ah = pygame.image.load('data/images/player/ahead/idle/140/0.gif')
player_idle_140_ah = pygame.transform.scale(player_idle_140_ah, (int(player_idle_140_ah.get_width() * SCALE),
                                                         int(player_idle_140_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_147_ah = pygame.image.load('data/images/player/ahead/idle/147/0.gif')
player_idle_147_ah = pygame.transform.scale(player_idle_147_ah, (int(player_idle_147_ah.get_width() * SCALE),
                                                         int(player_idle_147_ah.get_height() * SCALE))).convert_alpha(SCREEN)


player_idle_154_ah = pygame.image.load('data/images/player/ahead/idle/154/0.gif')
player_idle_154_ah = pygame.transform.scale(player_idle_154_ah, (int(player_idle_154_ah.get_width() * SCALE),
                                                         int(player_idle_154_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_161_ah = pygame.image.load('data/images/player/ahead/idle/161/0.gif')
player_idle_161_ah = pygame.transform.scale(player_idle_161_ah, (int(player_idle_161_ah.get_width() * SCALE),
                                                         int(player_idle_161_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_168_ah = pygame.image.load('data/images/player/ahead/idle/168/0.gif')
player_idle_168_ah = pygame.transform.scale(player_idle_168_ah, (int(player_idle_168_ah.get_width() * SCALE),
                                                         int(player_idle_168_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_175_ah = pygame.image.load('data/images/player/ahead/idle/175/0.gif')
player_idle_175_ah = pygame.transform.scale(player_idle_175_ah, (int(player_idle_175_ah.get_width() * SCALE),
                                                         int(player_idle_175_ah.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_13_bk = pygame.image.load('data/images/player/back/idle/13/0.gif')
player_idle_13_bk = pygame.transform.scale(player_idle_13_bk, (int(player_idle_13_bk.get_width() * SCALE),
                                                         int(player_idle_13_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_20_bk = pygame.image.load('data/images/player/back/idle/20/0.gif')
player_idle_20_bk = pygame.transform.scale(player_idle_20_bk, (int(player_idle_20_bk.get_width() * SCALE),
                                                         int(player_idle_20_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_27_bk = pygame.image.load('data/images/player/back/idle/27/0.gif')
player_idle_27_bk = pygame.transform.scale(player_idle_27_bk, (int(player_idle_27_bk.get_width() * SCALE),
                                                         int(player_idle_27_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_34_bk = pygame.image.load('data/images/player/back/idle/34/0.gif')
player_idle_34_bk = pygame.transform.scale(player_idle_34_bk, (int(player_idle_34_bk.get_width() * SCALE),
                                                         int(player_idle_34_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_41_bk = pygame.image.load('data/images/player/back/idle/41/0.gif')
player_idle_41_bk = pygame.transform.scale(player_idle_41_bk, (int(player_idle_41_bk.get_width() * SCALE),
                                                         int(player_idle_41_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_48_bk = pygame.image.load('data/images/player/back/idle/48/0.gif')
player_idle_48_bk = pygame.transform.scale(player_idle_48_bk, (int(player_idle_48_bk.get_width() * SCALE),
                                                      int(player_idle_48_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_55_bk = pygame.image.load('data/images/player/back/idle/55/0.gif')
player_idle_55_bk = pygame.transform.scale(player_idle_55_bk, (int(player_idle_55_bk.get_width() * SCALE),
                                                      int(player_idle_55_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_62_bk = pygame.image.load('data/images/player/back/idle/62/0.gif')
player_idle_62_bk = pygame.transform.scale(player_idle_62_bk, (int(player_idle_62_bk.get_width() * SCALE),
                                                      int(player_idle_62_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_69_bk = pygame.image.load('data/images/player/back/idle/69/0.gif')
player_idle_69_bk = pygame.transform.scale(player_idle_69_bk, (int(player_idle_69_bk.get_width() * SCALE),
                                                      int(player_idle_69_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_76_bk = pygame.image.load('data/images/player/back/idle/76/0.gif')
player_idle_76_bk = pygame.transform.scale(player_idle_76_bk, (int(player_idle_76_bk.get_width() * SCALE),
                                                      int(player_idle_76_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_83_bk = pygame.image.load('data/images/player/back/idle/83/0.gif')
player_idle_83_bk = pygame.transform.scale(player_idle_83_bk, (int(player_idle_83_bk.get_width() * SCALE),
                                                      int(player_idle_83_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_90_bk = pygame.image.load('data/images/player/back/idle/90/0.gif')
player_idle_90_bk = pygame.transform.scale(player_idle_90_bk, (int(player_idle_90_bk.get_width() * SCALE),
                                                      int(player_idle_90_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_97_bk = pygame.image.load('data/images/player/back/idle/97/0.gif')
player_idle_97_bk = pygame.transform.scale(player_idle_97_bk, (int(player_idle_97_bk.get_width() * SCALE),
                                                      int(player_idle_97_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_105_bk = pygame.image.load('data/images/player/back/idle/105/0.gif')
player_idle_105_bk = pygame.transform.scale(player_idle_105_bk, (int(player_idle_105_bk.get_width() * SCALE),
                                                      int(player_idle_105_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_112_bk = pygame.image.load('data/images/player/back/idle/112/0.gif')
player_idle_112_bk = pygame.transform.scale(player_idle_112_bk, (int(player_idle_112_bk.get_width() * SCALE),
                                                      int(player_idle_112_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_119_bk = pygame.image.load('data/images/player/back/idle/119/0.gif')
player_idle_119_bk = pygame.transform.scale(player_idle_119_bk, (int(player_idle_119_bk.get_width() * SCALE),
                                                      int(player_idle_119_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_126_bk = pygame.image.load('data/images/player/back/idle/126/0.gif')
player_idle_126_bk = pygame.transform.scale(player_idle_126_bk, (int(player_idle_126_bk.get_width() * SCALE),
                                                      int(player_idle_126_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_133_bk = pygame.image.load('data/images/player/back/idle/133/0.gif')
player_idle_133_bk = pygame.transform.scale(player_idle_133_bk, (int(player_idle_133_bk.get_width() * SCALE),
                                                      int(player_idle_133_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_140_bk = pygame.image.load('data/images/player/back/idle/140/0.gif')
player_idle_140_bk = pygame.transform.scale(player_idle_140_bk, (int(player_idle_140_bk.get_width() * SCALE),
                                                      int(player_idle_140_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_147_bk = pygame.image.load('data/images/player/back/idle/147/0.gif')
player_idle_147_bk = pygame.transform.scale(player_idle_147_bk, (int(player_idle_147_bk.get_width() * SCALE),
                                                      int(player_idle_147_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_154_bk = pygame.image.load('data/images/player/back/idle/154/0.gif')
player_idle_154_bk = pygame.transform.scale(player_idle_154_bk, (int(player_idle_154_bk.get_width() * SCALE),
                                                      int(player_idle_154_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_161_bk = pygame.image.load('data/images/player/back/idle/161/0.gif')
player_idle_161_bk = pygame.transform.scale(player_idle_161_bk, (int(player_idle_161_bk.get_width() * SCALE),
                                                      int(player_idle_161_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_168_bk = pygame.image.load('data/images/player/back/idle/168/0.gif')
player_idle_168_bk = pygame.transform.scale(player_idle_168_bk, (int(player_idle_168_bk.get_width() * SCALE),
                                                      int(player_idle_168_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_idle_175_bk = pygame.image.load('data/images/player/back/idle/175/0.gif')
player_idle_175_bk = pygame.transform.scale(player_idle_175_bk, (int(player_idle_175_bk.get_width() * SCALE),
                                                      int(player_idle_175_bk.get_height() * SCALE))).convert_alpha(SCREEN)

player_run_6_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/6/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_6_ah.append(image)

player_run_13_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/13/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_13_ah.append(image)

player_run_20_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/20/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_20_ah.append(image)

player_run_27_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/27/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_27_ah.append(image)

player_run_34_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/34/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_34_ah.append(image)

player_run_41_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/41/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_41_ah.append(image)

player_run_48_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/48/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_48_ah.append(image)

player_run_55_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/55/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_55_ah.append(image)

player_run_62_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/62/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_62_ah.append(image)


player_run_69_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/69/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_69_ah.append(image)

player_run_76_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/76/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_76_ah.append(image)

player_run_83_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/83/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_83_ah.append(image)

player_run_90_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/90/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_90_ah.append(image)

player_run_97_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/97/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_97_ah.append(image)

player_run_105_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/105/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_105_ah.append(image)

player_run_112_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/112/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_112_ah.append(image)

player_run_119_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/119/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_119_ah.append(image)

player_run_126_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/126/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_126_ah.append(image)

player_run_133_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/133/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_133_ah.append(image)

player_run_140_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/140/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_140_ah.append(image)

player_run_147_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/147/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_147_ah.append(image)

player_run_154_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/154/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_154_ah.append(image)

player_run_161_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/161/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_161_ah.append(image)

player_run_168_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/168/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_168_ah.append(image)

player_run_175_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/175/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_175_ah.append(image)

player_run_13_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/13/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_13_bk.append(image)

player_run_20_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/20/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_20_bk.append(image)


player_run_27_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/27/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_27_bk.append(image)


player_run_34_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/34/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_34_bk.append(image)


player_run_41_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/41/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_41_bk.append(image)


player_run_48_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/48/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_48_bk.append(image)


player_run_55_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/55/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_55_bk.append(image)


player_run_62_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/62/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_62_bk.append(image)


player_run_69_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/69/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_69_bk.append(image)


player_run_76_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/76/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_76_bk.append(image)


player_run_83_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/83/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_83_bk.append(image)


player_run_90_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/90/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_90_bk.append(image)


player_run_97_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/97/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_97_bk.append(image)

player_run_105_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/105/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_105_bk.append(image)


player_run_112_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/112/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_112_bk.append(image)


player_run_119_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/119/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_119_bk.append(image)


player_run_126_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/126/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_126_bk.append(image)


player_run_133_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/133/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_133_bk.append(image)


player_run_140_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/140/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_140_bk.append(image)


player_run_147_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/147/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_147_bk.append(image)


player_run_154_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/154/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_154_bk.append(image)


player_run_161_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/161/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_161_bk.append(image)


player_run_168_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/168/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_168_bk.append(image)


player_run_175_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/175/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    player_run_175_bk.append(image)

image = pygame.image.load('data/images/explosive/idle/0.png')
explosive_idle_image = pygame.transform.scale(image,
                                                  (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)

explosive_walk_images = []
for i in range(7):
    image = pygame.image.load(f'data/images/explosive/walk/{i}.png')
    image = pygame.transform.scale(image,
                                                  (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(SCREEN)
    explosive_walk_images.append(image)

desert_background_images = []
for i in range(3):
    image = pygame.image.load(f'data/images/level_objects/backgrounds/desert/layer_{i}.png')
    image = pygame.transform.scale(image,
                                   (int(image.get_width()) * 3.2, int(image.get_height()) * 3.2)).convert_alpha(SCREEN)
    desert_background_images.append(image)


explosion_2_images = []
for i in range(12):
    image = pygame.image.load(f'data/images/misc/explosion/2/{i}.png')
    image = pygame.transform.scale(image,
                                   (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(
        SCREEN)
    explosion_2_images.append(image)



image = pygame.image.load(f'data/images/projectiles/blue/90.gif')
blue_projectile = pygame.transform.scale(image,
                                   (int(image.get_width() * 1.4), int(image.get_height() * 1.4))).convert_alpha(
        SCREEN)

