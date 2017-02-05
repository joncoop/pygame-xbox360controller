# xBox360 Controller for Python3 with Pygame

This is a unified XBox360 wired controller module for use with Python3 and Pygame. It allows for games be developed and played cross-platform without worrying about how axes and buttons are mapped on different OSs.

## Requirements

On Linux and Windows systems, only Python 3 with Pygame is needed. Mac OSX does not have native controller support so the [driver from Tattiebogle](http://tattiebogle.net/index.php/ProjectRoot/Xbox360Controller/OsxDriver) is also requred.

#### Tested on:

- Python 3.4.3, 3.5.2 with Pygame 1.9.2, SDL (1, 2, 15)
- Ubuntu 15.04 & 16.04, Mac OSX 10.9.5, Windows 7, 8

## Usage

1. Download the `xbox360controller` class to your project folder and import into your game.

    ```python
    import xbox360_controller
    ```

2. Create a `Controller` object. The `id` argument must be a value from `0` to `pygame.joystick.get_count() - 1`.

    ```python
    controller = xbox360_controller.Controller(0)
    ```

3. Get the controller values.

    The `get_buttons()` function returns a tuple of boolean values representing the state of every button on the controller. Use the button constants to index the tuple. A `True` value means that the button is pressed.

    ```python
    pressed = controller.get_buttons()

    if pressed[xbox360_controller.START]:
        do_something()
    ```

    The following `xbox360_controller` button constants are supported:
    `A`, `B`, `X`, `Y`, `LEFT_BUMP`, `RIGHT_BUMP`, `BACK`, `START`, `LEFT_STICK_BTN`, and `RIGHT_STICK_BTN`.

    The functions `get_left_stick()` and `get_left_stick()` can be used to access the state of each analog stick. Each functin returns a tuple of float values containing the x and y values of the stick's axes. Values are in the range `-1.0 <= value <= 1.0` where negative values represent the left and up directions and positive values represent down and right directions.

    ```python
    left_x, left_y = controller.get_left_stick()
    right_x, right_y = controller.get_right_stick()
    ```

    The `get_pad()` function returns a tuple of boolean values representing the state of each of the four directions on the directional-pad in the order up, right, down, left (clockwise). A `True` value means that the pad is pressed in that direction. The pad is 8-directional, so it is possible that two directions return `True` at the same time.

    ```python
    pad_up, pad_right, pad_down, pad_left = controller.get_pad()
    ```

    The `get_triggers()` function returns a single float value in the range `-1.0 <= value <= 1.0`. A value of `-1.0` indicates full left trigger and `1.0` indicates full right trigger. Note that triggers are additive. Therefore pulling both triggers fully together will result in a value of `0`.

    ```python
    triggers = controller.get_triggers()
    ```

4. Make something awesome!

    See `simple_game_template.py` for an example of usage within a pygame project.

## Files:

- `xbox360_controller.py`

  This file contains the `Controller` class which can be used in Pygame projects.

- `visualizer.py`

  See the values returned by an `xbox360_controller` object on a graphical mockup of the controller.

- `simple_game.py`

  This demonstrates basic usage of the `xbox360_controller` class and can be used as a template for a game. Press 'start' to begin the game. The ball is controlled by the left stick. The 'A' button changes the ball's color. Pressing 'back' resets the game.

- `test.py`

  Plug in a controller and check out the raw values returned by each button/axis. This is just slightly modified example code from the official [Pygame joystick documentation](https://www.pygame.org/docs/ref/joystick.html). The `xbox360_controller` class is not used here. Rather, it is a useful tool to see how inputs are mapped on different platforms.

## Author

Designed and built by [joncoop](https://github.com/joncoop). He hopes you use this to make something cool.

## License

This project is distributed under the [MIT License](LICENSE.md).

## Acknowledgments

- Thanks to Nathan for doing the testing on his Mac.
- Thanks to [Max](https://github.com/DovahRahDoLu) for testing with wireless controllers on Windows.
