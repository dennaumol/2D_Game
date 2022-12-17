from settings import *


class Chunk:
    def __init__(self, left, top):
        self.rect = pygame.Rect(left, top, CHUNK_WIDTH, CHUNK_HEIGHT)
        self.objects = [[], []]



