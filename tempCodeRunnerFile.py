import sys
import os
from grid import create_grid, update_grid
from save import save_grid, load_grid
from terminal import clear_terminal

sys.stdout.reconfigure(encoding='utf-8')

# Initialiser une liste pour stocker les états de la grille
grid_history = []

# Demander à l'utilisateur s'il souhaite charger la grille sauvegardée ou créer une nouvelle grille
if os.path.exists("grid.txt"):
    choice = input("Do you want to load the saved grid? (y/n): ").strip().lower()
    if choice == 'y':
        grid_history = load_grid()
        grid = grid_history[-1]
        rows = len(grid)
        cols = len(grid[0])
    else:
        rows = int(input("Enter the size of the grid: "))
        cols = rows
        grid = create_grid(rows, cols)
else:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    grid = create_grid(rows, cols)

# Ajouter l'état initial de la grille à l'historique
grid_history.append(grid)

while True:
    clear_terminal()
    for line in grid:
        print('\u200A'.join(line))  # Ajouter un espace fin entre chaque cellule
    user_input = input("Press Enter to see the next generation or Q to quit: ").strip().lower()
    if user_input == 'q':
        save_grid(grid_history)  # Sauvegarder l'historique des grilles
        print("Grid saved. Exiting the program.")
        break
    grid = update_grid(grid)
    grid_history.append(grid)  # Ajouter la nouvelle grille à l'historique
    save_grid(grid_history)  # Sauvegarder l'historique des grilles après chaque mise à jour