import pygame

class Fuel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        This function initializes the Fuel object
        Args:
        Return: 
        None

        """
        super().__init__()
        
        self.image = pygame.image.load("assets/fuelcan.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y