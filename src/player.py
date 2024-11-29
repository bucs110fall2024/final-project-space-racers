import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        This function initializes the Player object
        Args:
        Return: 
        None

        """

        super().__init__()
        
        self.image = pygame.image.load("assets/ship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 7
        self.score = 0
    
    def move_left(self):
        """
        This function moves the Player left
        Args:
        Return: 
        None

        """
        self.rect.x -= self.speed
        
    def move_right(self):
        """
        This function moves the Player right
        Args:
        Return: 
        None

        """
        self.rect.x += self.speed
        
    def move_up(self):
        """
        This function moves the Player up
        Args:
        Return: 
        None

        """
        self.rect.y -= self.speed

    def move_down(self):
        """
        This function moves the Player down
        Args:
        Return: 
        None

        """
        self.rect.y += self.speed
        
    def add_score(self):
        """
        This function adds the player's score as they play
        Args:
        Return: 
        None

        """
        self.score += 1