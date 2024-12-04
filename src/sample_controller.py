import random
import pygame
import pygame_menu
from src.fuel import Fuel
from src.obstacle import Obstacle
from src.player import Player

MAX_OBSTACLES = 10
MAX_FUELCANS = 1
OBSTACLE_SPAWN_RATE = 3
FUEL_SPAWN_RATE = 10


class Controller:
    def __init__(self):
        """
        This function initializes the Controller object
        Args:
        Return:
        None

        """
        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()

        self.p1 = Player(self.width / 2, self.height - 100)
        self.obstacles = pygame.sprite.Group()
        self.max_obstacles = MAX_OBSTACLES
        self.fuel = pygame.sprite.Group()
        self.max_fuelcans = MAX_FUELCANS
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(
            self.background, pygame.display.get_window_size()
        )
        self.score = 0

        pygame.key.set_repeat(10)
        self.state = "START"

    def mainloop(self):
        """
        This function sets up the directory for the start menu, game, and game over functions
        Args:
        Return:
        None

        """
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.gameoverloop()
            elif self.state == "START":
                self.menuloop()

    def startgame(self):
        """
        This function changes the game state to game
        Args:
        Return:
        None

        """
        self.state = "GAME"

    def menuloop(self):
        """
        This function creates the start menu
        Args:
        Return:
        None

        """
        self.menu = pygame_menu.Menu("Space Racers", self.width / 2, self.height / 2)
        self.menu.add.label("Click START to play", font_size=28)
        self.menu.add.button(
            "START", self.startgame, align=pygame_menu.locals.ALIGN_CENTER
        )

        while self.state == "START":
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.menu.update(events)
            self.menu.draw(self.screen)
            pygame.display.flip()

    def gameloop(self):
        """
        This function runs all of the events and updates for the game itself
        Args:
        Return:
        None

        """
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.p1.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.p1.move_down()
                    elif event.key == pygame.K_LEFT:
                        self.p1.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.p1.move_right()

            if self.p1.rect.x > self.width - 100:
                self.p1.rect.x = self.width - 100
            elif self.p1.rect.x < 0:
                self.p1.rect.x = 0
            elif self.p1.rect.y > self.height - 100:
                self.p1.rect.y = self.height - 100
            elif self.p1.rect.y < 0:
                self.p1.rect.y = 0

            obstacle_chance = random.randint(1, 100)
            if (
                obstacle_chance <= OBSTACLE_SPAWN_RATE
                and len(self.obstacles) < self.max_obstacles
            ):
                self.obstacles.add(Obstacle(random.randint(0, self.width), -100))

            fuel_chance = random.randint(1, 100)
            if fuel_chance <= FUEL_SPAWN_RATE and len(self.fuel) < self.max_fuelcans:
                self.fuel.add(Fuel(random.randint(50, self.width - 50), -100))

            for obstacle in self.obstacles:
                if self.p1.rect.colliderect(obstacle):
                    self.state = "END"

            for fuelcan in self.fuel:
                if self.p1.rect.colliderect(fuelcan):
                    fuelcan.kill()
                    self.score += 1
                elif fuelcan.rect.y >= self.height:
                    self.state = "END"

            self.obstacles.update()
            self.fuel.update()

            self.screen.blit(self.background, (0, 0))
            self.obstacles.draw(self.screen)
            self.fuel.draw(self.screen)
            self.screen.blit(self.p1.image, self.p1.rect)
            score_font = pygame.font.SysFont(None, 48)
            score_message = score_font.render(f"Score: {self.score}", True, "red")
            self.screen.blit(score_message, (1650, 50))
            highscore_font = pygame.font.SysFont(None, 48)
            self.highscore = open("src/highscore.txt", "r")
            highscore = self.highscore.read()
            highscore_message = highscore_font.render(
                f"High Score: {highscore}", True, "red"
            )
            self.screen.blit(highscore_message, (1650, 100))
            self.highscore.close()
            
            pygame.display.flip()

    def gameoverloop(self):
        """
        This function displays the game over text, and updates the highscore if it is surpassed
        Args:
        Return:
        None

        """
        end_font = pygame.font.SysFont(None, 48)
        end_message = end_font.render("GAME OVER", True, "red")
        close_message = end_font.render("Press ESC to close game", True, "red")

        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                        
            self.highscore = open("src/highscore.txt", "r")
            highscore = self.highscore.read()
            self.highscore.close()
            if self.score > int(highscore):
                self.highscore = open("src/highscore.txt", "w")
                self.highscore.write(str(self.score))
                self.highscore.close()
            self.screen.blit(end_message, (50, 50))
            self.screen.blit(close_message, (50, 100))
            
            pygame.display.flip()