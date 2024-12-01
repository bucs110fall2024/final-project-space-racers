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
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
    
    def update(self):
        """
        This function moves the obstacles down the screen
        Args:
        Return: 
        None

        """
        self.rect.y += self.speed
        if self.rect.y > 1080:
            self.kill()