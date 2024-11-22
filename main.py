import sys
import os
from grid import create_grid, update_grid
from save import save_grid, load_grid
from terminal import clear_terminal

sys.stdout.reconfigure(encoding='utf-8')

grid_history = []

clear_terminal()
if os.path.exists("grid.txt"):
    choice = input("Do you want to load the saved grid? (y/n): ").strip().lower()
    if choice == 'y':
        grid_history = load_grid()
        grid = grid_history[-1]
        rows = len(grid)
        cols = len(grid[0])
    else:
        while True:
            try:
                rows = int(input("Enter the size of the grid (between 3 and 62): "))
                if 3 <= rows <= 62:
                    break
                else:
                    print("Invalid size. Please enter a number between 3 and 62.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        cols = rows
        grid = create_grid(rows, cols)
else:
    while True:
        try:
            rows = int(input("Enter the number of rows (between 3 and 62): "))
            if 3 <= rows <= 62:
                break
            
            else:
                print("Invalid size. Please enter a number between 3 and 62.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    cols = rows
    grid = create_grid(rows, cols)

grid_history.append(grid)

while True:
    clear_terminal()
    for line in grid:
        print('\u200A'.join(line))  
    user_input = input("Press Enter to see the next generation or Q to quit: ").strip().lower()
    if user_input == 'q':
        save_grid(grid_history)  
        print("Grid saved. Exiting the program.")
        break
    grid = update_grid(grid)
    
    if len(grid_history) >= 2 and (grid == grid_history[-1] or grid == grid_history[-2]):
        print("Warning: Recurrence detected in the grid state.")
        break
        
    grid_history.append(grid)  
    save_grid(grid_history)