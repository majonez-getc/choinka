## Christmas Tree with Random Colors

This Python project creates a dynamic, colorful Christmas tree displayed in the console. Each time the tree is redrawn, it uses a random color scheme, making for a fun and festive console decoration. You can adjust the size of the tree, and the program continuously redraws it every second. The tree's trunk remains a fixed yellow color, while the rest of the tree bursts with random colors.

**Features:**

* **Random Colors:** The branches are printed in a random color from a pre-defined list every time the tree is redrawn.
* **Console Decoration:** A colorful Christmas tree graces your terminal and continuously updates.
* **Cross-Platform:** The code works on both Windows and Unix-based systems (Linux/macOS).
* **Trunk Design:** The yellow trunk provides a nice contrast to the colorful branches.

**Requirements:**

* Python 3.x
* colorama library (for colored output in the terminal)

You can install the required library using:

```
pip install colorama
```

**How to Run:**

1. Clone or download the repository.
2. Install the required dependency: `pip install colorama`
3. Run the script: `python main.py`

The program will continuously redraw the Christmas tree, updating its appearance every second. Press Ctrl+C to stop the program.

**How It Works:**

* **Random Color:** The `random_color()` function chooses from red, green, yellow, cyan, magenta, and blue to assign a random color to each branch of the tree.
* **Clear Screen:** The `clear_screen()` function ensures that the terminal screen is cleared between each redraw, creating the illusion of a live Christmas tree.
* **Tree Construction:** The `draw_tree()` function calculates the correct number of spaces and stars (*) for each row to build the tree. The tree is then printed line by line, with the yellow trunk at the bottom.
* **Main Loop:** The program continuously draws the tree every second until the user stops it with Ctrl+C.

**License:**

This project is open-source and available under the MIT License.

**Contributions:**

We welcome contributions! Feel free to open an issue or pull request if you'd like to be part of the project!
