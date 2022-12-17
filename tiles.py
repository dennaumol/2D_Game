from images import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image, collision=True, platform=False, z_index=0):
        super(Tile, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)
        self.platform = platform
        self.type = self.name = LEVEL_OBJECT
        self.collision = collision
        self.z_index = z_index

    def draw(self, surface, scroll):
        surface.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))
        # pygame.draw.rect(surface, 'RED',
        # (self.rect.x - scroll[0], self.rect.y - scroll[1], self.rect.width, self.rect.height))









