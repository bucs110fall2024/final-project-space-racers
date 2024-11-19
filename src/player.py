import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        """
        This function initializes the Player object
        Args:
        Return: 
        None

        """

        super().__init__()
        
        self.image = pygame.image.load("assets/ship.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    def move_left(self):
        """
        This function moves the Player left
        Args:
        Return: 
        None

        """
        self.rect.x -= 1
        
    def move_right(self):
        """
        This function moves the Player right
        Args:
        Return: 
        None

        """
        self.rect.x += 1
        
    def move_up(self):
        """
        This function moves the Player up
        Args:
        Return: 
        None

        """
        self.rect.y -= 1

    def move_down(self):
        """
        This function moves the Player down
        Args:
        Return: 
        None

        """
        self.rect.x += 1