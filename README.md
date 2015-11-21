# xBox360 Controller for Python3 with Pygame

This is a unified XBox360 wired controller for use with Python3 with Pygame. It allows for games be developed and played cross-platform without worrying about how axes and buttons are mapped on different OSs.

## Requirements

Python 3 with Pygame

Mac OSX does not have native controller support. The following driver was used. Mapping to another
driver could be different.

[http://tattiebogle.net/index.php/ProjectRoot/Xbox360Controller/OsxDriver#toc1ss](http://tattiebogle.net/index.php/ProjectRoot/Xbox360Controller/OsxDriver#toc1ss)

## Tested on:

* Python 3.4.3
* Pygame 1.9.2, SDL (1, 2, 15)

* Mac OSX 10.9.5
* Ubuntu 15.04
* Windows 7

## Usage

1. Download the xbox360controller class to your game folder and import into your game.
        ```
        from xbox360_controller import XBox360Controller
        ```
2. Create a controller object.
        ```
        controller = XBox360Controller(0)
        ```
3. Get the controller values.
        ```
        back = controller.back()
        start = controller.start()
        lt_stick = controller.left_stick_axes()
        ```
4. Make something awesome!
        ```
        if start == 1:
            playing = True
        ```

See simple_game_template.py for an example of usage within a pygame project.

## Author

Jon Cooper

## License

This project is distributed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Thanks to Nathan for doing the testing on his Mac. 
* Thanks to Weston for getting Pygame configured on Nathan's Mac. Nathan sure hates that command-line stuff.

