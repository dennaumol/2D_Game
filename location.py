import random

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
    def __init__(self):
        self.x = CHUNK_WIDTH * 3
        self.y = CHUNK_HEIGHT * 3
        self.objects_with_collision = []
        self.cur_sand_variation = 0
        self.enemies = []
        self.all_location_objects = []
        self.dead_bottom = 0
        self.chunks = {}
        self.player_spawn = (self.x + CHUNK_WIDTH, self.y)

    def generate_sand_column(self):
        sand = eval(f'Tile(self.x, self.y, yellow_sand_{self.cur_sand_variation}_image, z_index=2)')
        top_sand = sand
        self.objects_with_collision.append(sand)
        if self.cur_sand_variation != 0:
            sand = eval(f'Tile(self.x, self.y - sand_block_size, yellow_sand_decoration_{self.cur_sand_variation}_image, collision=False, z_index=1)')
            self.all_location_objects.append(sand)
        self.cur_sand_variation += 1
        if self.cur_sand_variation > 3:
            self.cur_sand_variation = 0
        self.y += sand_block_size
        for i in range(10):
            self.all_location_objects.append(Tile(self.x, self.y, sand_block_image, collision=False, z_index=-1))
            self.y += sand_block_size
        for i in range(3):
            self.all_location_objects.append(eval(f'Tile(self.x, self.y, yellow_sand_under_{i}_image, collision=False, z_index=-1)'))
            self.y += sand_block_size
        return top_sand

    def generate(self):
        length = 1250
        for i in range(length):
            if randint(0, 10) == 0:
                self.all_location_objects.append(SmallMonster(self.x, self.y - 100))
            top_sand = self.generate_sand_column()
            self.x, self.y = top_sand.rect.x + sand_block_size, top_sand.rect.y
        self.all_location_objects.extend(self.objects_with_collision)

        self.calculate_location_rect()
        self.create_chunks()
        self.allocate_into_chunks()

    def calculate_location_rect(self):
        self.dead_bottom = max(self.all_location_objects, key=lambda object: object.rect.bottom).rect.bottom
        width = max(self.all_location_objects, key=lambda object: object.rect.x).rect.x + CHUNK_WIDTH * 3
        self.rect = pygame.Rect(0, 0, width, self.dead_bottom + CHUNK_HEIGHT * 3)

    def create_chunks(self):
        for chunk_row in range(self.rect.height // CHUNK_HEIGHT + 1):
            for chunk_col in range(self.rect.width // CHUNK_WIDTH + 1):
                chunk = Chunk(chunk_col * CHUNK_WIDTH, chunk_row * CHUNK_HEIGHT)
                self.chunks[(chunk_col, chunk_row)] = chunk

    def allocate_into_chunks(self):
        for object in self.all_location_objects:
            chunk_row = object.rect.y // CHUNK_HEIGHT
            chunk_col = object.rect.x // CHUNK_WIDTH
            if object in self.objects_with_collision:
                self.chunks[chunk_col, chunk_row].objects[0].append(object)
            elif object.type == ENTITY:
                self.chunks[chunk_col, chunk_row].objects[2].append(object)
            else:
                self.chunks[chunk_col, chunk_row].objects[1].append(object)

    def get_chunk_objects(self, chunk_col, chunk_row):
        return self.chunks[chunk_col, chunk_row].objects.copy()
































