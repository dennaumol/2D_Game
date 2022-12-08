from images import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image, platform=False):
        super(Tile, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)
        self.platform = platform
        self.type = LEVEL_OBJECT
        self.name = LEVEL_OBJECT

    def draw(self, surface, scroll):
        surface.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))
        # pygame.draw.rect(surface, 'RED',
        # (self.rect.x - scroll[0], self.rect.y - scroll[1], self.rect.width, self.rect.height))







