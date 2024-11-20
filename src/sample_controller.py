import pygame
from src.player import Player
from src.obstacle import Obstacle
from src.fuel import Fuel

class Controller:
  
  def __init__(self):
    self.screen = pygame.display.set_mode()
    
    self.p1 = Player()
    self.obstacles = pygame.sprite.Group()
    self.fuel = []
    self.state = "START"
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
      self.background = pygame.image.load("assets/background.png")
      
      #4 display
      
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    pass
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    pass
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
