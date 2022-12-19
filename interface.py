from settings import *

class HeathBar:
    def __init__(self) -> None:
        self.hp = 0

    def update(self, player):
        self.hp = player.hp
        self.max_hp = player.max_hp
        
    
    def draw(self, surface):
        pygame.draw.rect(surface, (61, 145, 75), pygame.Rect(20, 20, 300, 50))
        
        pygame.draw.rect(surface, 'GREEN', pygame.Rect(25, 25, 290 * self.hp / self.max_hp, 40))
    



    
