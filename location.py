from tiles import *
from random import *
from backgrounds import *



class Location:
    pass


column_width = gray_column_0_image.get_width()
column_height = gray_column_0_image.get_height()
block_size = yellow_sand_0_image.get_width()
column_top_height = gray_column_top_0_image.get_height()

COLUMNS = 'COLUMNS'
DESERT = 'DESERT'


class YellowDesert(Location):
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.start_x = start_x
        self.start_y = start_y
        self.front = []
        self.behind = []
        self.top = -500
        self.bottom = 500
        self.objects_with_collision = []
        self.first = True
        self.both_directions = choice([True, False])
        self.total_length = 20
        self.y_changing_frequency_desert = 13
        self.y_changing_frequency_columns = 1
        self.first_location = DESERT
        self.generate_background()
        if self.both_directions:
            self.direction = 1
        else:
            self.direction = choice([-1, 1])

    def generate_background(self):
        self.background = DesertBackground()

    def generate_desert(self, length=50):
        if not self.both_directions and self.first:
            column = self.generate_column()

            if self.direction == 1:
                self.x = column.rect.right + 1
            else:
                self.x = column.rect.left - block_size

        if not self.first and self.direction == -1:
            self.x += self.direction * block_size

        sand_variation = 0
        triple_platform_generated_count = 0
        if self.direction == -1:
            sand_variation = 3

        y_changed = self.y_changing_frequency_desert
        for i in range(length):
            if y_changed == 0:
                y_changed = self.y_changing_frequency_desert
                k = randint(0, 1)
                if k == 0 and not self.y - column_height < self.top:
                    self.y -= column_height
                    current_y = self.y
                    if self.direction == -1:
                        self.x = self.x - column_width + block_size
                    self.objects_with_collision.append(Tile(self.x, self.y - column_top_height,
                                                            eval(f'gray_column_top_{choice([0, 1])}_image')))
                    for i in range(50):
                        column = Tile(self.x, current_y, gray_column_0_image)
                        self.objects_with_collision.append(column)
                        if column.rect.bottom >= self.bottom:
                            break
                        current_y = column.rect.bottom

                    if self.direction == 1:
                        self.x = column.rect.right
                    else:
                        self.x = column.rect.left - block_size

                elif k == 1 and not self.y + column_height > 0:
                    current_y = self.y
                    if self.direction == -1:
                        self.x = self.x - column_width + block_size
                    self.objects_with_collision.append(Tile(self.x, self.y - column_top_height,
                                                            eval(f'gray_column_top_{choice([0, 1])}_image')))
                    for i in range(50):
                        column = Tile(self.x, current_y, gray_column_0_image)
                        self.objects_with_collision.append(column)
                        if column.rect.bottom >= self.bottom:
                            break
                        current_y = column.rect.bottom

                    self.y += column_height

                    if self.direction == 1:
                        self.x = column.rect.right
                    else:
                        self.x = column.rect.left - block_size


            sand_block = Tile(self.x, self.y, eval(f'yellow_sand_{sand_variation}_image'))
            self.objects_with_collision.append(sand_block)

            if sand_variation != 0:
                self.front.append(Tile(self.x, self.y - block_size,
                                  eval(f'yellow_sand_decoration_{sand_variation}_image')))
            if self.direction == 1:
                sand_variation += 1

            else:
                sand_variation -= 1

            if sand_variation == 4 and self.direction == 1:
                sand_variation = 0
            elif sand_variation == 0 and self.direction == -1:
                sand_variation = 3

            a = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

            if a == 0 and triple_platform_generated_count < 2:
                triple_platform_generated_count = 5
                platform = Tile(self.x, self.y - block_size * choice([3, 4]),
                                gray_single_flying_platform_image)
                self.objects_with_collision.append(platform)

            elif a == 1 and triple_platform_generated_count < 0:
                triple_platform_generated_count = 5
                platform = Tile(self.x, self.y - block_size * choice([3, 4]),
                                eval(f'gray_triple_flying_platform_{choice([0, 1])}_image'))
                self.objects_with_collision.append(platform)

            triple_platform_generated_count -= 1

            for j in range(50):
                self.behind.append(Tile(self.x, self.y + block_size * (j + 1), sand_block_image))
                if self.y + block_size * (j + 1) > self.bottom:
                    break

            if self.direction == -1:
                if i != length - 1:
                    self.x = sand_block.rect.left - block_size
                else:
                    self.x = sand_block.rect.left
            else:
                self.x = sand_block.rect.right

            y_changed -= 1

    def generate_column(self):
        column = Tile(self.x, self.y, gray_column_0_image)
        self.objects_with_collision.append(column)
        top_column = column
        column_top_height = gray_column_top_0_image.get_height()
        column_top = Tile(self.x, self.y - column_top_height, eval(f'gray_column_top_{choice([0, 1])}_image'))
        self.objects_with_collision.append(column_top)

        current_y = column.rect.bottom - 1
        for i in range(50):
            column = Tile(self.x, current_y, gray_column_0_image)
            self.objects_with_collision.append(column)
            current_y = column.rect.bottom - 1
            if column.rect.bottom >= self.bottom:
                break

        return top_column

    def generate_columns(self, length=5):
        if not self.first and self.direction == -1:
            self.x -= column_width


        column = self.generate_column()

        if self.direction == -1:
            self.x = column.rect.left - column_width - 1
        elif self.direction == 1:
            self.x = column.rect.right + 1

        y_changed = self.y_changing_frequency_columns

        for i in range(length):

            if y_changed == 0:
                k = randint(0, 1)
                if not self.y - column_height < self.top and k == 0:
                    self.y -= column_height
                    y_changed = self.y_changing_frequency_columns
                elif not self.y + column_height > self.bottom and k == 1:
                    self.y += column_height
                    y_changed = self.y_changing_frequency_columns

            if self.direction == -1:
                self.x = column.rect.left - column_width - 1 - choice([2, 3]) * column_width
            elif self.direction == 1:
                self.x = column.rect.right + 1 + choice([2, 3]) * column_width
            column = self.generate_column()
            y_changed -= 1

        if self.direction == -1:
            self.x = column.rect.left
        elif self.direction == 1:
            self.x = column.rect.right

    def generate(self):
        if not self.both_directions:
            for i in range(self.total_length):
                c = randint(0, 1)
                if c == 0:
                    self.generate_desert()
                    self.first = False
                else:
                    self.generate_columns()
                    self.first = False
        else:

            for i in range(self.total_length // 2):
                c = randint(0, 1)
                if c == 0:
                    self.generate_desert()
                    if self.first:
                        self.first_location = DESERT
                    self.first = False
                else:
                    self.generate_columns()
                    if self.first:
                        self.first_location = COLUMNS
                    self.first = False
            self.direction = -1
            self.x = self.start_x
            self.y = self.start_y
            self.first = True
            for i in range(self.total_length // 2):
                c = randint(0, 1)
                if c == 0:
                    if self.first_location == COLUMNS:
                        self.x -= block_size
                    self.generate_desert()
                    self.first = False
                else:
                    if self.first_location == COLUMNS:
                        self.x -= column_width * randint(1, 2)
                    self.generate_columns()
                    self.first = False

        return self.objects_with_collision, self.front, self.behind




















