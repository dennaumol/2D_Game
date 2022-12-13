import pygame

from tiles import *
from random import *
from backgrounds import *
from entities import SmallMonster
from chunks import *


class Border:
    def __init__(self, x, y, height):
        self.rect = pygame.Rect(0, 0, 1, height)
        self.rect.center = (x, y)
        self.name = BORDER
        self.type = LEVEL_OBJECT
        self.platform = False

    def draw(self, SCREEN, scroll):
        pass




class Location:
    pass


column_width = gray_column_0_image.get_width()
column_height = gray_column_0_image.get_height()
sand_block_size = yellow_sand_0_image.get_width()
column_top_height = gray_column_top_0_image.get_height()

COLUMNS = 'COLUMNS'
DESERT = 'DESERT'


class YellowDesert(Location):
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.objects_with_collision = []
        self.front = []
        self.behind = []
        self.cur_sand_variation = 0
        self.enemies = []
        self.all_location_objects = []
        self.bottom = start_y + 500

    def generate_sand_column(self):
        sand = eval(f'Tile(self.x, self.y, yellow_sand_{self.cur_sand_variation}_image)')
        top_sand = sand
        self.objects_with_collision.append(sand)
        if self.cur_sand_variation != 0:
            sand = eval(f'Tile(self.x, self.y - sand_block_size, yellow_sand_decoration_{self.cur_sand_variation}_image)')
            self.front.append(sand)
        self.cur_sand_variation += 1
        if self.cur_sand_variation > 3:
            self.cur_sand_variation = 0
        self.y += sand_block_size
        for i in range(2):
            self.behind.append(Tile(self.x, self.y, sand_block_image))
            self.y += sand_block_size
        for i in range(3):
            self.behind.append(eval(f'Tile(self.x, self.y, yellow_sand_under_{i}_image)'))
            self.y += sand_block_size
        return top_sand

    def generate(self):
        length = 2000
        for i in range(length):
            if randint(0, 10) == 0:
                self.enemies.append(SmallMonster(self.x, self.y - 100))
            top_sand = self.generate_sand_column()
            self.x, self.y = top_sand.rect.x + sand_block_size, top_sand.rect.y
        self.all_location_objects.extend(self.objects_with_collision)
        self.all_location_objects.extend(self.front)
        self.all_location_objects.extend(self.behind)


        return self.objects_with_collision, self.front, self.behind

    def init_location_rect(self):
        self.top_y = min(self.all_location_objects, key= lambda x: x.rect.top)
        self.left_x = min(self.all_location_objects, key=lambda x: x.rect.left)
        self.right_x = max(self.all_location_objects, key=lambda x: x.rect.right)
        self.bottom_y = max(self.all_location_objects, key=lambda x: x.rect.bottom)





















