from images import *


class Background:
    pass


class DesertBackground(Background):
    def __init__(self):
        self.images = desert_background_images


    def draw(self, surface):
        drawing_rect = self.images[0].get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2))
        for image in self.images:
            surface.blit(image, (drawing_rect.x, drawing_rect.y))

