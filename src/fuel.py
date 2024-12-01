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
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        
    def update(self):
        """
        This function moves the fuel objects down the screen
        Args:
        Return: 
        None

        """
        self.rect.y += self.speed
        if self.rect.y > 1080:
            self.kill()