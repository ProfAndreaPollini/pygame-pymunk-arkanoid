import pygame
from pygame.locals import *
from pygame.math import Vector2

import pymunk
import pymunk.pygame_util

import random

class Ball(pygame.sprite.Sprite):

  def __init__(self, x,y,radius):
    pygame.sprite.Sprite.__init__(self)
    self.r = radius
    self.image = pygame.Surface([radius, radius])
    #self.image.fill(0)
    pygame.draw.circle(self.image,Color(255,255,255),(self.r //2 ,self.r //2),self.r)  # type: ignore
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y
    self.direction = Vector2(1,0)
    self.velocity = 5
    self.x = x 
    self.y = y

    self._init_physics()

  def _init_physics(self):
    mass = 10
   
    inertia = pymunk.moment_for_circle(mass, 0, self.r, (0, 0))
    self.body = pymunk.Body(mass, inertia)
   
    self.body.position = self.x,self.y
    self.shape = pymunk.Circle(self.body, self.r, (0, 0))
    self.shape.elasticity = 1
    self.shape.friction = 0
    self.shape.collision_type = 0
    self.body.apply_impulse_at_local_point((self.velocity*(2*random.random()-1),self.velocity*(2*random.random()-1)))

  def update(self, dt):
   

    self.rect.x = self.body.position.x
    self.rect.y = self.body.position.y

  def handle_collision(self, collider) :
    ...