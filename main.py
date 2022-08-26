from dataclasses import dataclass
import pygame
from pygame.math import Vector2
from pygame import Color,Rect

# pymunk imports
import pymunk
import pymunk.pygame_util

from ball import Ball
from wall import Wall,WallInfo
from brick import Brick
from paddle import Paddle



walls  = [
  WallInfo(0.0,0.0,0.05,1),
  WallInfo(0.95,0.0,0.05,1),
  WallInfo(0.05,0.0,0.95,0.05),
  WallInfo(0.05,0.95,0.95,0.05)
]

def create_brick_grid( rect,width,height,spacing = 1):
  """
  Create a brick grid.
  :param screen:
  :param rect:
  :return:
  """
  brick_grid = []

  start_x = rect.left
  start_y = rect.top

  brick_w = width
  brick_h = height

  for x in range(rect.width):
    for y in range(rect.height):
      print(start_x + brick_w *x + spacing,start_y + brick_h*y + spacing,width,height)
      brick_grid.append(Brick(start_x + brick_w *x + spacing*x,start_y + brick_h*y + spacing*y,width,height))

  return brick_grid










pygame.init()

W = 1280
H = 720

screen = pygame.display.set_mode((W,H))

pygame.display.set_caption("Non ce la faremo mai: arkanoid in 1 ora")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
brick_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()


## PYMUNK INIT

space = pymunk.Space()
space.gravity = (0.0, 0.0) # no gravity

def post_solve_handler(arbiter, space: pymunk.Space,data):
  a, b = arbiter.shapes
  print(a, b)
  for brick in brick_sprites:
    if brick.rect.contains(b.body.position,(1,1)):
      brick.kill()
      break
  space.remove(b)

  


_draw_options = pymunk.pygame_util.DrawOptions(pygame.display.get_surface())  # type: ignore


for wall_info in walls:
  print(wall_info)
  wall = Wall(Rect(wall_info.x*W, wall_info.y*H, wall_info.width*W, wall_info.height*H))
  all_sprites.add(wall)
  wall_sprites.add(wall)
  space.add(wall.body,wall.shape)

paddle = Paddle(screen.get_rect())

all_sprites.add(paddle)
player_sprite.add(paddle)
space.add(paddle.body,paddle.shape)

bricks = create_brick_grid(Rect(100,100,20,5),50,20)
for brick in bricks:
  all_sprites.add(brick)
  brick_sprites.add(brick)
  space.add(brick.body,brick.shape)
  # space.reindex_shapes_for_body(brick.body)

ball = Ball(screen.get_rect().centerx,screen.get_rect().centery,10)
all_sprites.add(ball)
space.add(ball.body, ball.shape)

handler = space.add_collision_handler(0, 1)
    
handler.post_solve = post_solve_handler

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
  #update sprites
  dt = clock.tick(60)
  for _ in range(5):
    space.step(dt/5)
  all_sprites.update(dt)

  #clear screen
  screen.fill('black')

  #draw the sprites
  all_sprites.draw(screen)

  # space.debug_draw(_draw_options)

  collided_wall =  pygame.sprite.spritecollideany(ball,wall_sprites)

  if collided_wall:
    ball.handle_collision(collided_wall)
    print(collided_wall)
  
  pygame.display.update()
