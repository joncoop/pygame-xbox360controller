# xBox360 Controller for Python3 with Pygame

This is a unified XBox360 wired controller for use with Python3 and Pygame. It allows for games be developed and played cross-platform without worrying about how axes and buttons are mapped on different OSs.

## Requirements

On Linux and Windows systems, only Python 3 with Pygame is required.

Mac OSX does not have native controller support. The following driver was used. Mapping to another driver could be different.

[http://tattiebogle.net/index.php/ProjectRoot/Xbox360Controller/OsxDriver#toc1ss](http://tattiebogle.net/index.php/ProjectRoot/Xbox360Controller/OsxDriver#toc1ss)

#### Tested on:

- Python 3.4.3, 3.5.2 with
- Pygame 1.9.2, SDL (1, 2, 15)

- Mac OSX 10.9.5
- Ubuntu 15.04, 16.04
- Windows 7, 8

## Usage

1. Download the `xbox360controller` class to your game folder and import into your game.

    ```python
    import xbox360_controller
    ```

2. Create a controller object. The `id` argument must be a value from `0` to `pygame.joystick.get_count()-1`.

    ```python
    controller = xbox360_controller.Controller(0)
    ```

3. Get the controller values.

    To get button values, use the `get_buttons()` function which returns a sequence of boolean values representing the state of every button on the controller. Use the button constant values to index the array. A True value means that the button is pressed.

    ```python
    pressed = controller.get_buttons()

    if pressed[xbox360_controller.START]:
        play()
    ```

    The following xbox360_controller button constants are supported:
    `A`, `B`, `X`, `Y`, `LEFT_BUMP`, `RIGHT_BUMP`, `BACK`, `START`, `LEFT_STICK_BTN`, and `RIGHT_STICK_BTN`.

    Each analog stick returns a tuple of `float` values containing the `x` and `y` values of the axis. The values are in the range `-1.0 <= value <= 1.0` where negative values represent the left and up directions and positive values represent down and right directions.

    ```python
    left_x, left_y = controller.get_left_stick()
    right_x, right_y = controller.get_right_stick()
    ```

    To get directional pad values, use the `get_dpad()` function which returns a sequence of boolean values representing each of the four directions on the d-pad in the order up, right, down, left. A True value means that the D-pad is pressed in that direction. The D-pad is 8-directional, so it is possible that two directions return True at the same time.

    ```python
    d_up, d_right, d_down, d_left = controller.get_dpad()
    ```

    The `get_triggers()` function returns a single `float` value in the range `-1.0 <= value <= 1.0`. A value of `-1.0` indicates full left trigger and `1.0` indicates full right trigger. Note that triggers are additive. Therefore pulling both triggers fully together will result in a value of `0`.

    ```python
    triggers = controller.get_triggers()
    ```

4. Make something awesome!

    See `simple_game_template.py` for an example of usage within a pygame project.

## Files:

##### xbox360_controller.py

  This file contains the Controller class which can be used in Pygame projects.

##### visualizer.py

  See the values returned by an `xbox360_controller` object on a graphical mockup of the controller.

##### simple_game_template.py

  This demonstrates basic usage of the `xbox360_controller` class and can be used as a template for a game. Press 'start' to begin the game. The ball is controlled by the left stick. The 'A' button changes the ball's color. Pressing 'back' resets the game.

##### test.py

  Plug in a controller and check the raw values returned by each button/axis. This is just slightly modified joystick example code from the joystick documentation page. This does not use the `xbox360_controller`. Rather, it can be used to see how inputs are mapped on different platforms.

## Author

[joncoop](https://github.com/joncoop)

## License

This project is distributed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Thanks to Nathan for doing the testing on his Mac.
* Thanks to Weston for getting Pygame configured on Nathan's Mac. Nathan sure hates that command-line stuff.
