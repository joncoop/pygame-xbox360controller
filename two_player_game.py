#  Copyright (c) 2017 Jon Cooper
#
#  This file is part of pygame-xbox360controller.
#  Documentation, related files, and licensing can be found at
#
#      <https://github.com/joncoop/pygame-xbox360controller>.


import pygame
import xbox360_controller

pygame.init()

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# window settings
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simple Game")
FPS = 60
clock = pygame.time.Clock()

# make a controller
controller1 = xbox360_controller.Controller()
controller2 = xbox360_controller.Controller()

print(controller1.get_id(), controller2.get_id())

# make a ball
ball_1_pos = [250, 290]
ball_1_radius = 10
ball_1_color = WHITE

ball_2_pos = [330, 290]
ball_2_radius = 10
ball_2_color = WHITE

# settings
MAX_SPEED = 5

# game loop
playing = False
done = False

while not done:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

        if event.type == pygame.JOYBUTTONDOWN:
            # handle events for all controllers
            if not playing:
                if event.button == xbox360_controller.START:
                    playing = True
            else:
                if event.button == xbox360_controller.BACK:
                    playing = False
                    ball_1_pos = [250, 290]
                    ball_2_pos = [330, 290]

            # handle events for specific controllers
            if event.joy == controller1.get_id():
                if event.button == xbox360_controller.A:
                    if ball_1_color == WHITE:
                        ball_1_color = RED
                    else:
                        ball_1_color = WHITE
            elif event.joy == controller2.get_id():
                if event.button == xbox360_controller.A:
                    if ball_2_color == WHITE:
                        ball_2_color = RED
                    else:
                        ball_2_color = WHITE

    # handle joysticks
    x1, y1 = controller1.get_left_stick()
    x2, y2 = controller2.get_left_stick()

    # game logic
    if playing:
        ball_1_pos[0] += int(x1 * MAX_SPEED)
        ball_1_pos[1] += int(y1 * MAX_SPEED)

        ball_2_pos[0] += int(x2 * MAX_SPEED)
        ball_2_pos[1] += int(y2 * MAX_SPEED)

    # drawing
    screen.fill(BLACK)
    pygame.draw.circle(screen, ball_1_color, ball_1_pos, ball_1_radius)
    pygame.draw.circle(screen, ball_2_color, ball_2_pos, ball_2_radius)

    # update screen
    pygame.display.flip()
    clock.tick(FPS)

# close window on quit
pygame.quit ()
