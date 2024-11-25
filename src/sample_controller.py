import pygame
import pygame_menu
from src.player import Player
from src.obstacle import Obstacle
from src.fuel import Fuel

class Controller:
  
  def __init__(self):
    self.screen = pygame.display.set_mode()
    self.width, self.height = pygame.display.get_window_size()
    
    self.p1 = Player(500, 500)
    self.obstacles = pygame.sprite.Group()
    self.fuel = pygame.sprite.Group()
    self.state = "GAME"
    self.background = pygame.image.load("assets/background.png")
    self.background = pygame.transform.scale(self.background, pygame.display.get_window_size())
    self.p1.image = pygame.transform.scale(self.p1.image, (100, 100))
    pygame.key.set_repeat(10)
    #setup pygame data
    
  def mainloop(self):
    while True:
      if self.state == "GAME":
        self.gameloop()
      elif self.state == "START":
        self.menuloop()
      elif self.state == "END":
        self.gameoverloop()
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
      #event loop

      #update data
    
      self.screen.blit(self.background, (0, 0))
      self.screen.blit(self.p1.image, self.p1.rect)
      pygame.display.flip()
      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
