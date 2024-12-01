import pygame
import pygame_menu
import random
from src.player import Player
from src.obstacle import Obstacle
from src.fuel import Fuel

MAX_OBSTACLES = 10
MAX_FUELCANS = 1
OBSTACLE_SPAWN_RATE = 3
FUEL_SPAWN_RATE = 10

class Controller:
  
  def __init__(self):
    self.screen = pygame.display.set_mode()
    self.width, self.height = pygame.display.get_window_size()
    
    self.p1 = Player(self.width/2, self.height-100)
    self.obstacle = Obstacle(0,0)
    self.obstacles = pygame.sprite.Group()
    self.max_obstacles = MAX_OBSTACLES
    self.fuel = pygame.sprite.Group()
    self.max_fuelcans = MAX_FUELCANS
    self.background = pygame.image.load("assets/background.png")
    self.background = pygame.transform.scale(self.background, pygame.display.get_window_size())

    pygame.key.set_repeat(10)
    self.state = "GAME"
    #setup pygame data
    
  def mainloop(self):
    while True:
      if self.state == "GAME":
        self.gameloop()
      elif self.state == "END":
        self.gameoverloop()
      elif self.state == "START":
        self.menuloop()
      #1 event loop
      #2 updates
      #3 redraw (completely overlay the screen to prevent artifacts)

      
      #4 display
      
    #select state loop
    
  
  ### below are some sample loop states ###

  def startgame(self):
    self.startgame = "GAME"
    
  def menuloop(self):
    self.menu = pygame_menu.Menu("Space Racers", self.width / 2, self.height / 2)
    self.menu.add.label("Click START to play", font_size=28)
    self.menu.add.button("START", self.startgame, align=pygame_menu.locals.ALIGN_CENTER)

    while self.state == "START":
      self.menu.update(pygame.event.get())
      self.menu.draw(self.screen)
      pygame.display.flip()
    #bug: menu doesn't work

      #event loop

      #update data

      #redraw
      
  def gameloop(self):
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
      
      # Sets world borders for the player
      if self.p1.rect.x > self.width - 100:
        self.p1.rect.x = self.width - 100
      elif self.p1.rect.x < 0:
        self.p1.rect.x = 0
      elif self.p1.rect.y > self.height - 100:
        self.p1.rect.y = self.height - 100
      elif self.p1.rect.y < 0:
        self.p1.rect.y = 0
            
      #event loop

      #update data
      obstacle_chance = random.randint(1, 100)
      if obstacle_chance <= OBSTACLE_SPAWN_RATE and len(self.obstacles) < self.max_obstacles:
        self.obstacles.add(Obstacle(random.randint(0, self.width), -100))
        
      fuel_chance = random.randint(1, 100)
      if fuel_chance <= FUEL_SPAWN_RATE and len(self.fuel) < self.max_fuelcans:
        self.fuel.add(Fuel(random.randint(0, self.width), -100))
        
      for obstacle in self.obstacles:
        if self.p1.rect.colliderect(obstacle):
          self.state = "END"
      #bug: obstacles have too big of a hitbox
          
      for fuelcan in self.fuel:
        if self.p1.rect.colliderect(fuelcan):
          fuelcan.kill()
        elif fuelcan.rect.y >= 1080:
          self.state = "END"
        
      score = self.p1.add_score()
      #bug: score displays as NONE
        
      self.obstacles.update()
      self.fuel.update()
      
      self.screen.blit(self.background, (0, 0))
      self.obstacles.draw(self.screen)
      self.fuel.draw(self.screen)
      self.screen.blit(self.p1.image, self.p1.rect)
      score_font = pygame.font.SysFont(None, 48)
      score_message = score_font.render(f"Score:{score}", True, "red")
      self.screen.blit(score_message, (1700, 50))
      
      
      pygame.display.flip()
      #redraw
    
  def gameoverloop(self):
      end_font = pygame.font.SysFont(None, 48)
      end_message = end_font.render("GAME OVER", True, "red")

      while self.state == "END":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        self.screen.blit(end_message, (50, 50))
        pygame.display.flip()
      #event loop

      #update data

      #redraw
