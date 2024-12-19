Christmas Tree with Random Colors
This project creates a dynamic, colorful Christmas tree using Python, which is displayed in the console. Each time the tree is redrawn, it is shown with a random color scheme, making for a fun and festive console decoration. You can adjust the size of the tree and the program continuously redraws it every second. The tree's trunk is fixed in a yellow color, while the rest of the tree is generated with random colors.

Features
Random Colors: Each time the tree is redrawn, the branches are printed in a random color from a pre-defined list.
Console Decoration: A colorful Christmas tree is drawn and continuously updated in the terminal.
Cross-Platform: The code works on both Windows and Unix-based systems (Linux/macOS).
Trunk Design: The trunk is drawn in yellow, providing a nice contrast to the colorful branches.
Requirements
Python 3.x
colorama library (for colored output in the terminal)
You can install the required library using:
pip install colorama
How to Run
Clone or download the repository.
Install the required dependencies by running pip install colorama.
Run the script:
python christmas_tree.py
The program will continuously redraw the Christmas tree, updating its appearance every second. You can stop the program by pressing Ctrl+C.

How It Works
Random Color: The program randomly selects a color for each branch of the tree using the random_color() function, which chooses from red, green, yellow, cyan, magenta, and blue.
Clear Screen: The clear_screen() function ensures that the terminal screen is cleared between each redraw, giving the appearance of a "live" Christmas tree.
Tree Construction: The draw_tree() function builds the tree by calculating the correct number of spaces and stars (*) for each row. The tree is then printed line by line, with the trunk at the bottom.
Main Loop: The main loop continuously draws the tree every second until the user stops it with Ctrl+C.

Each time the tree is redrawn, the color of the branches changes.

License
This project is open-source and available under the MIT License.

Contributions
Feel free to open an issue or pull request if you would like to contribute to the project!
