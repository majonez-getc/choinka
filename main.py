import random
import time
import os
from colorama import Fore, init
import sys

# Initialize colorama for colored output
init(autoreset=True)
# Ensure UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

def random_color():
    """Selects a random color from the available options."""
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]
    return random.choice(colors)

def clear_screen():
    """Clears the console screen."""
    if os.name == 'nt':  # For Windows systems
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')

def draw_tree(rows):
    """Draws a colorful Christmas tree with the specified number of rows."""
    tree = []
    for i in range(1, rows + 1):
        if i == 1: # handle top row to prevent extra spacing.
            tree.append(' ' * (rows - i) + '*' * (2 * i - 1))
        else:
            tree.append(' ' * (rows - i + 1) + '*' * (2 * i - 1))

    # Create the tree trunk
    trunk_width = 8
    trunk_padding = (2 * rows - 1 - trunk_width) // 2
    trunk = f"{' ' * trunk_padding}{Fore.YELLOW}||||||||\n{' ' * trunk_padding}{Fore.YELLOW}||||||||\n{' ' * trunk_padding}{Fore.YELLOW}||||||||"
    tree.append(trunk)

    clear_screen()

    # Print the tree with random colors for each line
    for line in tree:
        if '||||' in line:  # Print trunk in yellow
            print(line)
        else:  # Print other lines in random colors
            print(random_color() + line)


try:
    rows = 40 # set how big the tree is.
    while True: # Continuously redraw the tree
        draw_tree(rows)
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt: # Allow user to exit with Ctrl+C
    print("\nProgram terminated.")