import random
import time
import os
from colorama import Fore, init
import sys

init(autoreset=True)
sys.stdout.reconfigure(encoding='utf-8')

def random_color():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]
    return random.choice(colors)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw_tree(rows):
    tree = []
    for i in range(1, rows + 1):
        if i == 1:
            tree.append(' ' * (rows - i) + '*' * (2 * i - 1))
        else:
            tree.append(' ' * (rows - i + 1) + '*' * (2 * i - 1))

    trunk_width = 8
    trunk_padding = (2 * rows - 1 - trunk_width) // 2
    trunk = f"{' ' * trunk_padding}{Fore.YELLOW}||||||||\n{' ' * trunk_padding}{Fore.YELLOW}||||||||\n{' ' * trunk_padding}{Fore.YELLOW}||||||||"
    tree.append(trunk)

    clear_screen()

    for line in tree:
        if '||||' in line:
            print(line)
        else:
            print(random_color() + line)


try:
    rows = 40
    while True:
        draw_tree(rows)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram zakończony.")