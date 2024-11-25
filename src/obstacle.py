import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        This function initializes the Obstacle object
        Args:
        Return: 
        None

        """
        super().__init__()
        
        self.image = pygame.image.load("assets/meteor.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
    
    def update(self):
        """
        This function moves the obstacles down the screen
        Args:
        Return: 
        None

        """
        self.rect.y += self.speed