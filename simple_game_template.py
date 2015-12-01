#  Copyright (c) 2015 Jon Cooper
#   
#  This file is part of pygame-xbox360controller.
#  Documentation, related files, and licensing can be found at
# 
#      <https://github.com/joncoop/pygame-xbox360controller>.


import pygame
from xbox360_controller import XBox360Controller

pygame.init()

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# window settings
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simple Game")
FPS = 30
clock = pygame.time.Clock()

# make a controller
controller = XBox360Controller(0)

# make a ball
ball_pos = [290, 290]
ball_radius = 10

ball_pos2 =[250, 250]

# game loop
playing = False
done = False

while not done:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    # joystick stuff
    back = controller.back()
    start = controller.start()
    lt_stick = controller.left_stick_axes()
    rt_stick = controller.right_stick_axes()

    # game logic
    if not playing:
        if start == 1:
            playing = True
    else:
        if back == 1:
            playing = False
            ball_pos = [290, 290]

    if playing:
        ball_pos[0] += int(lt_stick[0] * 10)
        ball_pos[1] += int(lt_stick[1] * 10)
        
        ball_pos2[0] += int(rt_stick[0] * 10)
        ball_pos2[1] += int(rt_stick[1] * 10)

    # drawing
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (ball_pos[0], ball_pos[1]), ball_radius)
    pygame.draw.circle(screen, (0, 255, 0), (ball_pos2[0], ball_pos2[1]), ball_radius)

    # update screen
    pygame.display.flip()
    clock.tick(FPS)

# close window on quit
pygame.quit ()
