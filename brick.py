
import pygame
from pygame.locals import *
from pygame.math import Vector2

import pymunk
import pymunk.pygame_util


class Brick(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height):
    pygame.sprite.Sprite.__init__(self)
    self.x = x
    self.y = y
    
    # Create an image of the block, and fill it with a color.
    # This could also be an image loaded from the disk.
    self.image = pygame.Surface([width, height])
    self.image.fill('red')
    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()
    self.translate(x,y)
    self._init_physics(self.rect)
    

  def _init_physics(self,rect):
    mass = 10

    # vertices = [(rect.x, rect.y),(rect.x + rect.w, rect.y),(rect.x + rect.w, rect.y + rect.h),(rect.x, rect.y + rect.h),(rect.x, rect.y)]
    # print(vertices)

    vertices = [(-rect.w//2, -rect.h//2),(rect.w//2, -rect.h//2),(rect.w//2, rect.h//2),(-rect.w//2, rect.h//2)]
   
    inertia = pymunk.moment_for_poly(mass, vertices )
    self.body = pymunk.Body(mass, 0,pymunk.Body.STATIC)
   
    self.body.position = rect.x + rect.w//2 , rect.y + rect.h//2
    self.shape = pymunk.Poly(self.body,vertices)
    self.shape.elasticity = 1
    self.shape.collision_type = 1
  

  def translate(self, x, y):
    self.rect.x = x
    self.rect.y = y

