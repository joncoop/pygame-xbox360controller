# xBox360 Controller for Python3 with Pygame

This is a unified XBox360 wired controller module for use with Python3 and Pygame. It allows for games be developed and played cross-platform without worrying about how axes and buttons are mapped on different OSs. The syntax is nearly identical to that used for dealing with the keyboard in Pygame. Therefore, the syntax should be simple and familiar.

## Requirements

On Linux and Windows systems, only Python 3 with Pygame is needed.

Mac OSX does not have native controller support so the a driver is needed.

For Mac OS 10.10 (Yosemite) and later, use the driver [360Controller](https://github.com/360Controller/360Controller).

Earlier versions of Mac OS may work with the original driver from [Tattiebogle](http://tattiebogle.net/index.php/ProjectRoot/Xbox360Controller/OsxDriver). However this driver is no longer maintained.

#### Tested on:

- Python 3.4.3 & 3.5.2 with Pygame 1.9.2, SDL (1, 2, 15)
- Ubuntu 15.04 & 16.04, Windows 7 & 8, Mac OS 10.9.5, 10.10.5.

## Usage

1. Download the `xbox360controller` class to your project folder and import into your game.

    ```python
    import xbox360_controller
    ```

2. Create a `Controller` object. The `id` argument must be a value from `0` to `pygame.joystick.get_count() - 1`.

    ```python
    my_controller = xbox360_controller.Controller(0)
    ```

3. Get the controller values.

    #### Buttons

    The `get_buttons()` function returns a tuple of int values representing the state of every button on the controller. Use the button constants to index the tuple. A value of `1` means that the button is pressed, and `0` is unpressed.

    ```python
    pressed = my_controller.get_buttons()

    if pressed[xbox360_controller.START]:
        do_something()
    ```

    Buttons can also be handled as `JOYBUTTONDOWN` events which have a button attribute.

    ```python
    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == xbox360_controller.A:
            do_something()
    ```

    The following `xbox360_controller` button constants are supported:
    `A`, `B`, `X`, `Y`, `LEFT_BUMP`, `RIGHT_BUMP`, `BACK`, `START`, `LEFT_STICK_BTN`, and `RIGHT_STICK_BTN`.

    #### Joysticks

    The functions `get_left_stick()` and `get_left_stick()` can be used to access the state of each analog stick. Each function returns a tuple of float values containing the x and y values of the stick's axes. Values are in the range `-1.0 <= value <= 1.0` where negative values represent the left and up directions and positive values represent down and right directions.

    ```python
    left_x, left_y = my_controller.get_left_stick()
    right_x, right_y = my_controller.get_right_stick()
    ```

    #### Directional pad

    The `get_pad()` function returns a tuple of int values representing the state of each of the four directions on the directional-pad in the order up, right, down, left (clockwise). A value of `1` means that the pad is pressed in that direction, and `0` is unpressed. The pad is 8-directional, so it is possible that two directions return `1` at the same time.

    ```python
    pad_up, pad_right, pad_down, pad_left = my_controller.get_pad()
    ```

    #### Triggers

    The `get_triggers()` function returns the state of the triggers as a single float value in the range `-1.0 <= value <= 1.0`. A value of `-1.0` indicates full left trigger and `1.0` indicates full right trigger. Note that triggers are additive. Therefore pulling both triggers fully together will result in a value of `0`.

    ```python
    triggers = my_controller.get_triggers()
    ```

4. Make something awesome!

    See `simple_game_template.py` for an example of usage within a pygame project.

## Files:

#### xbox360_controller.py

  This module contains the `Controller` class which can be used in Pygame projects.

#### visualizer.py

  See the values returned by an `xbox360_controller` object on a graphical mockup of the controller.

#### simple_game.py

  This demonstrates basic usage of the `xbox360_controller` and can be used as a template for a game. Press 'start' to begin the game. The ball is controlled by the left stick. The 'A' button changes the ball's color. Pressing 'back' resets the game.

#### test.py

  Plug in a controller and check out the raw values returned by each button/axis. This is just slightly modified example code from the official [Pygame joystick documentation](https://www.pygame.org/docs/ref/joystick.html). The `xbox360_controller` module is not used here. Rather, this module is a useful tool to see how inputs are mapped on different platforms.

## Author

[joncoop](https://github.com/joncoop) made this. He hopes you use it to make something cool.

## License

This project is distributed under the [MIT License](LICENSE.md).

## Acknowledgments

- Thanks to [Jordan](https://github.com/johoule) and Nathan for doing the testing on Macs.
- Thanks to [Max](https://github.com/DovahRahDoLu) for testing with wireless controllers on Windows.
