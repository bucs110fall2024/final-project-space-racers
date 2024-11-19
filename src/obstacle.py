import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, ):
        """
        This function initializes the Obstacle object
        Args:
        Return: 
        None

        """
        super().__init__()
        
        self.image = pygame.image.load("assets/meteor.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0