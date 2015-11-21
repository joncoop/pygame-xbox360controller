import pygame
from xbox360_controller import XBox360Controller

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 65, 65)
GREEN = (75, 225, 25)
BLUE = (65, 65, 255)
AMBER = (255, 175, 0)
GREY = (175, 175, 175)


pygame.init()

size = [600, 670]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("X-Box 360 Controller")

FPS = 30
clock = pygame.time.Clock()


# make a controller (should this be in the game loop?)
controller = XBox360Controller(0)


def display_text(screen, text, x, y):
    my_font = pygame.font.Font(None, 30)
    output = my_font.render(text, True, WHITE)
    screen.blit(output, [x, y])

# game loop
done = False

while not done:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    # joystick stuff
    a_btn = controller.a()
    b_btn = controller.b()
    x_btn = controller.x()
    y_btn = controller.y()
    back = controller.back()
    start = controller.start()
    lt_bump = controller.left_bumper()
    rt_bump = controller.right_bumper()
    triggers = controller.triggers()
    lt_stick = controller.left_stick_axes()
    rt_stick = controller.right_stick_axes()
    lt_stick_btn = controller.left_stick_button()
    rt_stick_btn = controller.right_stick_button()
    hat = controller.hat()

    # game logic


    # drawing
    screen.fill(BLACK)

    ''' controller outline '''
    pygame.draw.rect(screen, GREY, [40, 20, 520, 320], 3)
    

    ''' a, b, x, y '''
    x, y = 450, 120
    
    if a_btn == 1:
        pygame.draw.ellipse(screen, GREEN, [x + 30, y + 60, 25, 25])
    else:
        pygame.draw.ellipse(screen, GREEN, [x + 30, y + 60, 25, 25], 2)

    if b_btn == 1:
        pygame.draw.ellipse(screen, RED, [x + 60, y + 30, 25, 25])
    else:
        pygame.draw.ellipse(screen, RED, [x + 60, y + 30, 25, 25], 2)

    if x_btn == 1:
        pygame.draw.ellipse(screen, BLUE, [x, y + 30, 25, 25])
    else:
        pygame.draw.ellipse(screen, BLUE, [x, y + 30, 25, 25], 2)

    if y_btn == 1:
        pygame.draw.ellipse(screen, AMBER, [x + 30, y, 25, 25])
    else:
        pygame.draw.ellipse(screen, AMBER, [x + 30, y, 25, 25], 2)


    ''' back, start '''
    x, y = 250, 145
    
    if back == 1:
        pygame.draw.ellipse(screen, WHITE, [x, y, 25, 20])
    else:
        pygame.draw.ellipse(screen, WHITE, [x, y, 25, 20], 2)

    pygame.draw.ellipse(screen, GREY, [x + 40, y - 10, 40, 40])
    
    if start == 1:
        pygame.draw.ellipse(screen, WHITE, [x + 95, y, 25, 20])
    else:
        pygame.draw.ellipse(screen, WHITE, [x + 95, y, 25, 20], 2)


    ''' bumpers '''
    x, y = 100, 50
    
    if lt_bump == 1:
        pygame.draw.rect(screen, WHITE, [x, 50, y, 25])
    else:
        pygame.draw.rect(screen, WHITE, [x, 50, y, 25], 2)

    if rt_bump == 1:
        pygame.draw.rect(screen, WHITE, [x + 365, y, 50, 25])
    else:
        pygame.draw.rect(screen, WHITE, [x + 365, y, 50, 25], 2)

    ''' triggers '''
    x, y = 210, 60
    
    trigger_x = x + 100 + round(triggers * 100)
    pygame.draw.line(screen, WHITE, [x, y], [x + 200, y])
    pygame.draw.line(screen, WHITE, [trigger_x, y - 10], [trigger_x, y + 10])

    ''' left stick '''
    x, y = 65, 100
    
    left_x = x + 50 + round(lt_stick[0] * 50)
    left_y = y + 50 + round(lt_stick[1] * 50)
    
    pygame.draw.line(screen, WHITE, [x + 60, y], [x + 60, y + 120], 1)
    pygame.draw.line(screen, WHITE, [x, y + 60], [x + 120, y + 60], 1)
    if lt_stick_btn == 0:
        pygame.draw.ellipse(screen, WHITE, [left_x, left_y, 20, 20], 2)
    else:
        pygame.draw.ellipse(screen, WHITE, [left_x, left_y, 20, 20])

    ''' right stick '''
    x, y = 330, 190
    
    right_x = x + 50 + round(rt_stick[0] * 50)
    right_y = y + 50 + round(rt_stick[1] * 50)
    
    pygame.draw.line(screen, WHITE, [x + 60, y], [x + 60, y + 120], 1)
    pygame.draw.line(screen, WHITE, [x, y + 60], [x + 120, y + 60], 1)
    if rt_stick_btn == 0:
        pygame.draw.ellipse(screen, WHITE, [right_x, right_y, 20, 20], 2)
    else:
        pygame.draw.ellipse(screen, WHITE, [right_x, right_y, 20, 20])
  
    ''' hat '''
    x, y = 180, 200
    
    pygame.draw.ellipse(screen, WHITE, [x, y, 100, 100])
    if hat[0] == -1:
        pygame.draw.ellipse(screen, GREY, [x, y + 40, 20, 20])
    elif hat[0] == 1:
        pygame.draw.ellipse(screen, GREY, [x + 80, y + 40, 20, 20])
    if hat[1] == -1:
        pygame.draw.ellipse(screen, GREY, [x + 40, y, 20, 20])
    elif hat[1] == 1:
        pygame.draw.ellipse(screen, GREY, [x + 40, y +80, 20, 20])


    ''' joystick values '''
    x, y = 50, 370
    display_text(screen, "BUTTONS".format(a_btn), x, y)
    display_text(screen, "A: {}".format(a_btn), x, y+ 25)
    display_text(screen, "B: {}".format(b_btn), x, y + 50)
    display_text(screen, "X: {}".format(x_btn), x, y + 75)
    display_text(screen, "Y: {}".format(y_btn), x, y + 100)
    display_text(screen, "LB: {}".format(lt_bump), x, y + 125)
    display_text(screen, "RB: {}".format(rt_bump), x, y + 150)
    display_text(screen, "Back: {}".format(back), x, y + 175)
    display_text(screen, "Start: {}".format(start), x, y + 200)
    display_text(screen, "LT Stick Btn: {}".format(lt_stick_btn), x, y + 225)
    display_text(screen, "RT Stick Btn: {}".format(rt_stick_btn), x, y + 250)

    display_text(screen, "AXES".format(a_btn), x + 275, y)
    display_text(screen, "Left Stick: ({}, {})".format(round(lt_stick[0], 2), round(lt_stick[1], 2)), x + 275, y + 25)
    display_text(screen, "Right Stick: ({}, {})".format(round(rt_stick[0], 2), round(rt_stick[1], 2)), x + 275, y + 50)
    display_text(screen, "Triggers: {}".format(round(triggers, 2)), x + 275, y + 75)

    display_text(screen, "HATS".format(a_btn), x + 275, y + 125)
    display_text(screen, "Hat: {}".format(hat), x + 275, y + 150)

    pygame.display.flip()


    # limit refresh rate
    clock.tick(FPS)

# close window on quit
pygame.quit ()
