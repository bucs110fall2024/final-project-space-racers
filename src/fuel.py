import pygame

class Fuel(pygame.sprite.Sprite):
    def __init__(self, ):
        """
        This function initializes the Fuel object
        Args:
        Return: 
        None

        """
        super().__init__()
        
        self.image = pygame.image.load("assets/fuelcan.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0