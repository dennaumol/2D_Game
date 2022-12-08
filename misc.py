from images import *


class Explosion:
    def __init__(self, x, y):
        self.tick = 0
        self.type = MISC
        self.images = explosion_2_images
        self.image = self.images[0]
        self.rect = self.images[0].get_bounding_rect()
        self.rect.center = (x, y)
        self.damage = False
        self.name = EXPLOSION
        self.end = False

    def update(self, *args, **kwargs):
        self.image = self.images[self.tick // 6]
        self.tick += 1
        if self.tick >= 61:
            self.end = True
            self.tick = 0
        entities = kwargs['entities']

        if not self.damage:
            self.damage = True
            for entity in entities:
                if entity.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                    entity.take_damage(300)

    def draw(self, surface, scroll):
        image_rect = self.image.get_rect(centerx=self.rect.centerx - scroll[0], bottom=self.rect.bottom - scroll[1])
        #pygame.draw.rect(surface, "red", (self.rect.x - scroll[0], self.rect.y - scroll[1], self.rect.width, self.rect.height))
        surface.blit(self.image, image_rect)













