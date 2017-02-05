#  Copyright (c) 2017 Jon Cooper
#
#  This file is part of pygame-xbox360controller.
#  Documentation, related files, and licensing can be found at
#
#      <https://github.com/joncoop/pygame-xbox360controller>.


import pygame
import sys

LINUX = 0
MAC = 1
WINDOWS = 2

if sys.platform.startswith("lin"):
    platform_id = LINUX
elif sys.platform.startswith("darwin"):
    platform_id = MAC
elif sys.platform.startswith("win"):
    platform_id = WINDOWS

if platform_id == LINUX:
    # buttons
    A = 0
    B = 1
    X = 2
    Y = 3
    LEFT_BUMP = 4
    RIGHT_BUMP = 5
    BACK = 6
    START = 7
    # GUIDE = 8
    LEFT_STICK_BTN = 9
    RIGHT_STICK_BTN = 10

    # axes
    LEFT_STICK_X = 0
    LEFT_STICK_Y = 1
    RIGHT_STICK_X = 3
    RIGHT_STICK_Y = 4
    LEFT_TRIGGER = 2
    RIGHT_TRIGGER = 5

elif platform_id == WINDOWS:
    # buttons
    A = 0
    B = 1
    X = 2
    Y = 3
    LEFT_BUMP = 4
    RIGHT_BUMP = 5
    BACK = 6
    START = 7
    LEFT_STICK_BTN = 8
    RIGHT_STICK_BTN = 9

    # axes
    LEFT_STICK_X = 0
    LEFT_STICK_Y = 1
    RIGHT_STICK_X = 4
    RIGHT_STICK_Y = 3
    TRIGGERS = 2

elif platform_id == MAC:
    # buttons
    A = 11
    B = 12
    X = 13
    Y = 14
    LEFT_BUMP = 8
    RIGHT_BUMP = 9
    BACK = 5
    START = 4
    LEFT_STICK_BTN = 6
    RIGHT_STICK_BTN = 7

    # d-pad
    PAD_UP = 0
    PAD_DOWN = 1
    PAD_LEFT = 2
    PAD_RIGHT = 3

    # axes
    LEFT_STICK_X = 0
    LEFT_STICK_Y = 1
    RIGHT_STICK_X = 2
    RIGHT_STICK_Y = 3
    LEFT_TRIGGER = 4
    RIGHT_TRIGGER = 5

class Controller:

    def __init__(self, id, dead_zone = 0.15):
        """
        Initializes a controller.

        Args:
            id: The ID of the controller which must be a value from `0` to
                `pygame.joystick.get_count() - 1`
            dead_zone: The size of dead zone for the analog sticks (default 0.15)
        """

        self.joystick = pygame.joystick.Joystick(id)
        self.joystick.init()
        self.dead_zone = dead_zone

        # Linux and Mac triggers behave funny. See get_triggers().
        self.left_trigger_used = False
        self.right_trigger_used = False

    def get_id(self):
        """
        Returns:
            The ID of the controller. This is the same as the ID passed into
            the initializer.
        """

        return self.joystick.get_id()

    def dead_zone_adjustment(self, value):
        """
        Analog sticks likely wont ever return to exact center when released. Without
        a dead zone, it is likely that a small axis value will cause game objects
        to drift. This adjusment allows for a full range of input while still
        allowing a little bit of 'play' in the dead zone.

        Returns:
            Axis value outside of the dead zone remapped proportionally onto the
            -1.0 <= value <= 1.0 range.
        """

        if value > self.dead_zone:
            return (value - self.dead_zone) / (1 - self.dead_zone)
        elif value < -self.dead_zone:
            return (value + self.dead_zone) / (1 - self.dead_zone)
        else:
            return 0

    def get_buttons(self):
        """
        Gets the state of each button on the controller.

        Returns:
            A tuple with the state of each button. 1 is pressed, 0 is unpressed.
        """

        if platform_id == LINUX:
            return (self.joystick.get_button(A),
                    self.joystick.get_button(B),
                    self.joystick.get_button(X),
                    self.joystick.get_button(Y),
                    self.joystick.get_button(LEFT_BUMP),
                    self.joystick.get_button(RIGHT_BUMP),
                    self.joystick.get_button(BACK),
                    self.joystick.get_button(START),
                    0, # Unused, since Guide only works on Linux
                    self.joystick.get_button(LEFT_STICK_BTN),
                    self.joystick.get_button(RIGHT_STICK_BTN))

        elif platform_id == WINDOWS:
            return (self.joystick.get_button(A),
                    self.joystick.get_button(B),
                    self.joystick.get_button(X),
                    self.joystick.get_button(Y),
                    self.joystick.get_button(LEFT_BUMP),
                    self.joystick.get_button(RIGHT_BUMP),
                    self.joystick.get_button(BACK),
                    self.joystick.get_button(START),
                    self.joystick.get_button(LEFT_STICK_BTN),
                    self.joystick.get_button(RIGHT_STICK_BTN))

        elif platform_id == MAC:
            return (0, # Unused
                    0, # Unused
                    0, # Unused
                    0, # Unused
                    self.joystick.get_button(START),
                    self.joystick.get_button(BACK),
                    self.joystick.get_button(LEFT_STICK_BTN),
                    self.joystick.get_button(RIGHT_STICK_BTN),
                    self.joystick.get_button(LEFT_BUMP),
                    self.joystick.get_button(RIGHT_BUMP),
                    0, # Unused
                    self.joystick.get_button(A),
                    self.joystick.get_button(B),
                    self.joystick.get_button(X),
                    self.joystick.get_button(Y))

    def get_left_stick(self):
        """
        Gets the state of the left analog stick.

        Returns:
            The x & y axes as a tuple such that

            -1 <= x <= 1 && -1 <= y <= 1

            Negative values are left and up.
            Positive values are right and down.
        """

        left_stick_x = self.dead_zone_adjustment(self.joystick.get_axis(LEFT_STICK_X))
        left_stick_y = self.dead_zone_adjustment(self.joystick.get_axis(LEFT_STICK_Y))

        return (left_stick_x, left_stick_y)

    def get_right_stick(self):
        """
        Gets the state of the right analog stick.

        Returns:
            The x & y axes as a tuple such that

            -1 <= x <= 1 && -1 <= y <= 1

            Negative values are left and up.
            Positive values are right and down.
        """

        right_stick_x = self.dead_zone_adjustment(self.joystick.get_axis(RIGHT_STICK_X))
        right_stick_y = self.dead_zone_adjustment(self.joystick.get_axis(RIGHT_STICK_Y))

        return (right_stick_x, right_stick_y)

    def get_triggers(self):
        """
        Gets the state of the triggers.

        On Windows, both triggers work additively to return a single axis, whereas
        triggers on Linux and Mac function as independent axes. In this interface,
        triggers will behave additively for all platforms so that pygame controllers
        will work consistently on each platform.

        Also note that the value returned is on Windows is multiplied by -1 so that
        negative is to the left and positive to the right to be consistent with
        stick axes.

        On Linux and Mac, trigger axes return 0 if they haven't been used yet. Once
        used, an unpulled trigger returns 1 and pulled returns -1. The trigger_used
        booleans keep the math right for triggers prior to use.

        Returns:
            A float in the range -1.0 <= value <= 1.0 where -1.0 represents full
            left and 1.0 represents full right. If the triggers are pulled
            simultaneously, then the sum of the trigger pulls is returned.
        """

        trigger_axis = 0.0

        if platform_id == LINUX or platform_id == MAC:
            left = self.joystick.get_axis(LEFT_TRIGGER)
            right = self.joystick.get_axis(RIGHT_TRIGGER)

            if left != 0:
                self.left_trigger_used = True
            if right != 0:
                self.right_trigger_used = True

            if not self.left_trigger_used:
                left = -1
            if not self.right_trigger_used:
                right = -1

            trigger_axis = (-1 * left + right) / 2

        elif platform_id == WINDOWS:
            trigger_axis = -1 * self.joystick.get_axis(TRIGGERS)

        return trigger_axis

    def get_pad(self):
        """
        Gets the state of the directional pad.

        Returns:
            A tuple in the form (up, right, down, left) where each value will be
            1 if pressed, 0 otherwise. Pads are 8-directional, so it is possible
            to have up to two 1s in the returned tuple.
        """

        if platform_id == LINUX or platform_id == WINDOWS:
            hat_x, hat_y = self.joystick.get_hat(0)

            up = int(hat_y == 1)
            right = int(hat_x == 1)
            down = int(hat_y == -1)
            left = int(hat_x == -1)

        elif platform_id == MAC:
            up = self.joystick.get_button(PAD_UP)
            right = self.joystick.get_button(PAD_RIGHT)
            down = self.joystick.get_button(PAD_DOWN)
            left = self.joystick.get_button(PAD_LEFT)

        return up, right, down, left
