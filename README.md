# xBox360 Controller for Python3 with Pygame

This is a unified XBox360 wired controller for use with Python3 with Pygame. It allows for games be developed and played cross-platform without worrying about how axes and buttons are mapped on different OSs.

## Requirements

Python 3 with Pygame

Mac OSX does not have native controller support. The following driver was used. Mapping to another driver could be different.

[http://tattiebogle.net/index.php/ProjectRoot/Xbox360Controller/OsxDriver#toc1ss](http://tattiebogle.net/index.php/ProjectRoot/Xbox360Controller/OsxDriver#toc1ss)

## Tested on:

- Python 3.4.3, 3.5.2 with
- Pygame 1.9.2, SDL (1, 2, 15)

- Mac OSX 10.9.5,
- Ubuntu 15.04, 16.04
- Windows 7

## Usage

1. Download the xbox360controller class to your game folder and import into your game.

  ```python
  import xbox360_controller
  ```

2. Create a controller object.

  ```python
  controller = xbox360_controller.Controller(0)
  ```

3. Get the controller values.

  ```python
  pressed = controller.get_buttons()
  ```

4. Make something awesome!

  ```python
  if pressed[xbox360_controller.START]:
      play()
  ```

  The following xbox360_controller button constants are supported:
  `A`, `B`, `X`, `Y`, `LEFT_BUMP`, `RIGHT_BUMP`, `BACK`, `START`, `LEFT_STICK_BTN`, and `RIGHT_STICK_BTN`.

See `simple_game_template.py` for an example of usage within a pygame project.

## Files:

### xbox360_controller.py

The controller class which can be used in pygame projects.

### visualizer.py

See the values returned by an xbox360_controller object on a graphical mockup of the controller.

### simple_game_template.py

This demonstrates usage of the `xbox360_controller` class and can be used as a template for a game. Press 'start' to begin the game. The ball in the middle is controlled by the left stick. The 'A' button changes the balls color. Pressing 'back' resets the game.

### test.py

Plug in a controller and check the raw values returned by each button/axis. This is just slightly modified joystick example code from the joystick documentation page. This does not use the xbox360_controller. Rather, it can be used to see how inputs are mapped on different platforms.

## Author

joncoop

## License

This project is distributed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Thanks to Nathan for doing the testing on his Mac.
* Thanks to Weston for getting Pygame configured on Nathan's Mac. Nathan sure hates that command-line stuff.
