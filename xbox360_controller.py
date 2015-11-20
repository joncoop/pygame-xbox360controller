'''
Unified XBox360 wired* controller interface for Python with Pygame.

Versions:
Python 3.4.3
Pygame 1.9.2, SDL (1, 2, 15)

Tested on:
Mac OSX 10.9.5
Ubuntu 15.04
Windows 7

Mac OSX does not have native controller support. The following driver was used. Mapping to another
driver could be different.

http://tattiebogle.net/index.php/ProjectRoot/Xbox360Controller/OsxDriver#toc1ss

* On Linux, only wired controllers use axes for the hat; wireless use buttons. Wireless support
  not included yet.

'''

import pygame
import sys

LINUX = 0
MAC = 1
WINDOWS = 2

class XBox360Controller:
    
    def __init__(self, num):
        if sys.platform.startswith("lin"):
            self.platform_id = LINUX
        elif sys.platform.startswith("darwin"):
            self.platform_id = MAC
        elif sys.platform.startswith("win"):
            self.platform_id = WINDOWS
        
        if self.platform_id == LINUX:
            # buttons
            self.A = 0
            self.B = 1
            self.X = 2
            self.Y = 3
            self.LEFT_BUMP = 4
            self.RIGHT_BUMP = 5
            self.BACK = 6
            self.START = 7
            self.LEFT_STICK_BTN = 9
            self.RIGHT_STICK_BTN = 10

            # axes
            self.LEFT_STICK_X = 0
            self.LEFT_STICK_Y = 1
            self.RIGHT_STICK_X = 3
            self.RIGHT_STICK_Y = 4
            self.LEFT_TRIGGER = 2
            self.RIGHT_TRIGGER = 5

        elif self.platform_id == MAC:
            # buttons
            self.A = 11
            self.B = 12
            self.X = 13
            self.Y = 14
            self.LEFT_BUMP = 8
            self.RIGHT_BUMP = 9
            self.BACK = 5
            self.START = 4
            self.LEFT_STICK_BTN = 6
            self.RIGHT_STICK_BTN = 7
            self.HAT_UP = 0
            self.HAT_DOWN = 1
            self.HAT_LEFT = 2
            self.HAT_RIGHT = 3	

            # axes
            self.LEFT_STICK_X = 0
            self.LEFT_STICK_Y = 1
            self.RIGHT_STICK_X = 2
            self.RIGHT_STICK_Y = 3
            self.LEFT_TRIGGER = 4
            self.RIGHT_TRIGGER = 5
    
        elif self.platform_id == WINDOWS:
            # buttons
            self.A = 0
            self.B = 1
            self.X = 2
            self.Y = 3
            self.LEFT_BUMP = 4
            self.RIGHT_BUMP = 5
            self.BACK = 6
            self.START = 7
            self.LEFT_STICK_BTN = 8
            self.RIGHT_STICK_BTN = 9

            # axes
            self.LEFT_STICK_X = 0
            self.LEFT_STICK_Y = 1
            self.RIGHT_STICK_X = 3
            self.RIGHT_STICK_Y = 4
            self.TRIGGERS = 2

        self.joystick = pygame.joystick.Joystick(num)
        self.joystick.init()
        self.dead_zone = 0.15

        self.left_trigger_used = False
        self.right_trigger_used = False
        
    def dead_zone_adjust(self, value):
	"""
	Proportionally adjusts axis values on sticks so that areas outside deadzone 
        still return values from 0.0 to 1.0. For example, if the deadzone is set to 
        0.15, then an axis value of 0.15 or less will return 0, and 1.0 will return 1.0. 
	"""
        
	if value > self.dead_zone:
            return (value - self.dead_zone) / (1 - self.dead_zone)
        elif value < -self.dead_zone:
            return (value + self.dead_zone) / (1 - self.dead_zone)
        else:
            return 0
        
    def a(self):
        """
        Returns 1 if A button is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.A)

    def b(self):
        """
        Returns 1 if B button is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.B)

    def x(self):
        """
        Returns 1 if X button is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.X)

    def y(self):
        """
        Returns 1 if Y button is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.Y)
    
    def left_bumper(self):
        """
        Returns 1 if left bumper is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.LEFT_BUMP)

    def right_bumper(self):
        """
        Returns 1 if right bumper is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.RIGHT_BUMP)

    def back(self):
        """
        Returns 1 if Back button is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.BACK)

    def start(self):
        """
        Returns 1 if Start button is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.START)

    def left_stick_button(self):
        """
        Returns 1 if left stick button is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.LEFT_STICK_BTN)

    def right_stick_button(self):
        """
        Returns 1 if right stick button is pressed, 0 otherwise.
        """

        return self.joystick.get_button(self.RIGHT_STICK_BTN)

    def left_stick_axes(self):
        """
        Returns the x & y axes as a tuple such that

            -1 <= x <= 1 && -1 <= y <= 1

        Negative values are left and up.
        Positive values are right and down.
        """
        
        left_stick_x = self.dead_zone_adjust(self.joystick.get_axis(self.LEFT_STICK_X))
        left_stick_y = self.dead_zone_adjust(self.joystick.get_axis(self.LEFT_STICK_Y))

        return (left_stick_x, left_stick_y)

    def right_stick_axes(self):
        """
        Returns the x & y axes as a tuple such that

            -1 <= x <= 1 && -1 <= y <= 1

        Negative values are left and up.
        Positive values are right and down.
        """

        right_stick_x = self.dead_zone_adjust(self.joystick.get_axis(self.RIGHT_STICK_X))
        right_stick_y = self.dead_zone_adjust(self.joystick.get_axis(self.RIGHT_STICK_Y))       
            
        return (right_stick_x, right_stick_y)

    def triggers(self):
        """
        The triggers also form an axis. Full left trigger returns -1 and full right returns +1.
        If the triggers are pulled simultaneously, then the sum of the trigger pulls is returned.

        Notes:
        On Windows, both triggers work additively to return a single axis, whereas triggers on
        Linux and Mac function as independent axes. In this interface, triggers will behave
        additively for all platforms so that pygame controllers will work consistently on each
        platform.
        
        Also note that the value returned is on windows is multiplied by -1 so that negative is to
        the left and positive to the right to be consistent with stick axes.

        On Linux and Mac, trigger axes return 0 if they haven't been used yet. Once used, an unpulled
        trigger returns 1 and pulled returns -1. The trigger_used booleans keep the math right for
        triggers prior to use.
        """

        trigger_axis = 0.0
        
        if self.platform_id == LINUX or self.platform_id == MAC:
            left = self.joystick.get_axis(self.LEFT_TRIGGER)
            right = self.joystick.get_axis(self.RIGHT_TRIGGER)

            if left != 0:
                self.left_trigger_used = True
            if right != 0:
                self.right_trigger_used = True

            if not self.left_trigger_used:
                left = -1
            if not self.right_trigger_used:
                right = -1
                
            trigger_axis = (-1 * left + right) / 2
            
        elif self.platform_id == WINDOWS:
            trigger_axis = -1 * self.joystick.get_axis(self.TRIGGERS)
            
        return trigger_axis


    def hat(self):
        """
        The directional pad is a hat. The hat is returns an ordered pair as a tuple. Each value is
        the set {-1, 0, 1}. The first value will be -1 if the hat is pressed on the left, and 1 if
        pressed on the right. The second value will be -1 if the hat is pressed down and 1 if
        pressed up.

        Notes:
        On Linux and Windows, the y value is multiplied by -1 to make it consistent with joystick
        direction mapping.

        The hat on a Mac is interpreted as 4 independent buttons with each returning either 0 or 1.
        Button values are added to make tuple consistent with Linux/Windows behavior.
        """

        if self.platform_id == LINUX or self.platform_id == WINDOWS:
            hat_x = self.joystick.get_hat(0)[0]
            hat_y = -1 * self.joystick.get_hat(0)[1]
        elif self.platform_id == MAC:
            hat_x = -1 * self.joystick.get_button(self.HAT_LEFT) + self.joystick.get_button(self.HAT_RIGHT)
            hat_y = -1 * self.joystick.get_button(self.HAT_UP) + self.joystick.get_button(self.HAT_DOWN)

        return (hat_x, hat_y)
