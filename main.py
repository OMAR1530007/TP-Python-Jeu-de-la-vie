import sys
import os
import time
from grid import create_grid, update_grid
from save import save_grid, load_grid
from terminal import clear_terminal

sys.stdout.reconfigure(encoding='utf-8')

def initialize_game():
    clear_terminal()
    grid_history = []

    if not os.path.exists("grid_save.txt"):
        with open("grid_save.txt", "w") as f:
            pass  

    if os.stat("grid_save.txt").st_size == 0:
        rows, cols, grid = create_new_grid()
    else:
        while True:
            try:
                clear_terminal()
                choice = input("Do you want to load the saved grid? (y/n): ").strip().lower()
                if choice == 'y':
                    grid_history = load_grid()
                    grid = grid_history[-1]
                    rows = len(grid)
                    cols = len(grid[0])
                    break
                elif choice == 'n':
                    rows, cols, grid = create_new_grid()
                    break
                else:
                    print("Please enter a valid choice.")
                    time.sleep(1)
            except Exception as e:
                print(f"An error occurred: {e}")
                time.sleep(1)

    grid_history.append(grid)
    return grid, grid_history
        

def create_new_grid():
    
    while True:
        try:
            clear_terminal()
            rows = int(input("Enter the size of the grid (between 3 and 62): "))
            if 3 <= rows <= 62:
                break
            else:
                print("Invalid size. Please enter a number between 3 and 62.")
                time.sleep(1)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            time.sleep(1)
    cols = rows
    grid = create_grid(rows, cols)
    return rows, cols, grid

def play_game():

    grid, grid_history = initialize_game()

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
            print("Pattern detected. Exiting the program.")
            break

        grid_history.append(grid)
        save_grid(grid_history)

if __name__ == "__main__":
    play_game()
