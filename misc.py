from images import *


class Explosion:
    def __init__(self, x, y):
        self.z_index = 100
        self.tick = 0
        self.type = MISC
        self.images = explosion_2_images
        self.image = self.images[0]
        self.rect = self.images[6].get_bounding_rect()
        self.rect.center = (x, y)
        self.damage_rect = self.rect
        self.damage_rect.width *= 1
        self.damage_rect.height *= 1
        self.damage_rect.center = self.rect.center
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
                if entity.rect.colliderect(self.damage_rect):
                    entity.take_damage(1000)

    def draw(self, surface, scroll):
        image_rect = self.image.get_rect(centerx=self.rect.centerx - scroll[0], bottom=self.rect.bottom - scroll[1])
        #pygame.draw.rect(surface, "red", (self.damage_rect.x - scroll[0], self.damage_rect.y - scroll[1], self.damage_rect.width, self.damage_rect.height))
        surface.blit(self.image, image_rect)











