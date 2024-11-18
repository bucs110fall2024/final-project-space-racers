import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        
        self.image = pygame.image.load("assets/ship.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    def move_left(self):
        self.rect.x -= 1
        
    def move_right(self):
        self.rect.x += 1
        
    def move_up(self):
        self.rect.y -= 1

    def move_down(self):
        self.rect.x += 1