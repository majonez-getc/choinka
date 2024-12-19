import random
import time
import os
from colorama import Fore, init

# Inicjalizacja coloramy
init(autoreset=True)

# Funkcja do generowania losowego koloru
def random_color():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]
    return random.choice(colors)

# Funkcja rysująca choinkę
def draw_tree():
    tree = [
        "       *",
        "       ***",
        "      *****",
        "     *******",
        "    *********",
        "   ***********",
        "  *************",
        " ***************",
        "      |||"
    ]

    # Rysowanie choinki z losowymi kolorami
    os.system('cls' if os.name == 'nt' else 'clear')  # Czyszczenie ekranu
    for line in tree:
        print(random_color() + line)  # Każda linia choinki ma inny kolor

# Główna pętla programu
try:
    while True:
        draw_tree()  # Rysowanie choinki
        time.sleep(1)  # Odczekaj 1 sekundę przed rysowaniem nowej choinki
except KeyboardInterrupt:
    print("\nProgram zakończony.")
