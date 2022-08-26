from dataclasses import dataclass
import pygame
from pygame.locals import *
from pygame.math import Vector2

import pymunk
import pymunk.pygame_util

@dataclass
class WallInfo:
  x: float
  y: float
  width: float
  height: float

class Wall(pygame.sprite.Sprite):

 # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self,rect):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    # Create an image of the block, and fill it with a color.
    # This could also be an image loaded from the disk.
    self.image = pygame.Surface((rect.w, rect.h))
    self.image.fill(Color(200,0,200))
    

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()
    self.rect.x = rect.x
    self.rect.y = rect.y
    self._init_physics(self.rect)

  def _init_physics(self,rect):
    mass = 10

    # vertices = [(rect.x, rect.y),(rect.x + rect.w, rect.y),(rect.x + rect.w, rect.y + rect.h),(rect.x, rect.y + rect.h),(rect.x, rect.y)]
    # print(vertices)

    vertices = [(-rect.w//2, -rect.h//2),(rect.w//2, -rect.h//2),(rect.w//2, rect.h//2),(-rect.w//2, rect.h//2)]
   
    # inertia = pymunk.moment_for_poly(mass, vertices )
    self.body = pymunk.Body(mass, 0.0,pymunk.Body.STATIC)
   
    self.body.position = rect.x + rect.w//2, rect.y + rect.h//2
    self.shape = pymunk.Poly(self.body,vertices)
    self.shape.elasticity = 1
  
    

