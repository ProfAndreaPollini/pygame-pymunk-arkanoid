import pygame
from pygame.locals import *
from pygame.math import Vector2

import pymunk
import pymunk.pygame_util



class Paddle(pygame.sprite.Sprite):

  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self,screen_rect):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    # Create an image of the block, and fill it with a color.
    # This could also be an image loaded from the disk.
    self.image = pygame.Surface([80, 16])
    self.image.fill('red')

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()
    self.center(screen_rect)
    self._init_physics(self.rect)
    

  def _init_physics(self,rect):
    mass = 10

    # vertices = [(rect.x, rect.y),(rect.x + rect.w, rect.y),(rect.x + rect.w, rect.y + rect.h),(rect.x, rect.y + rect.h),(rect.x, rect.y)]
    # print(vertices)

    vertices = [(-rect.w//2, -rect.h//2),(rect.w//2, -rect.h//2),(rect.w//2, rect.h//2),(-rect.w//2, rect.h//2)]
   
    inertia = pymunk.moment_for_poly(mass, vertices )
    self.body = pymunk.Body(mass, inertia)
   
    self.body.position = rect.x + rect.w//2 , rect.y + rect.h//2
    
    self.shape = pymunk.Poly(self.body,vertices)
    self.shape.elasticity = 1
    self.shape.collision_type = 1
    
  

  def translate(self, x, y):
    self.rect.x = x
    self.rect.y = y
    
  def center(self, screen_rect):
   
    self.rect.y = screen_rect.midbottom[1] *0.9
    self.rect.x = screen_rect.midbottom[0] 


  def update(self,dt):
    key_pressed = pygame.key.get_pressed()

    self.rect.x = self.body.position.x
    self.rect.y = self.body.position.y
   
    #chek if left key is pressed
    if key_pressed[pygame.K_LEFT]:
      self.body.apply_impulse_at_local_point((-0.01,0))
    if key_pressed[pygame.K_RIGHT]:
      self.body.apply_impulse_at_local_point((0.01,0))  
    
