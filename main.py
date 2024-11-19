import sys
import random
import os

sys.stdout.reconfigure(encoding='utf-8')

def create_grid(rows, cols):
    grid = []
    for _ in range(rows):
        line = [random.choice(['⬛', '⬜']) for _ in range(cols)]
        grid.append(line)
    return grid

def neighbor_alive(grid, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    alive_count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == '⬜':
                alive_count += 1
    return alive_count

def is_alive(grid, row, col):
    alive_neighbors = neighbor_alive(grid, row, col)
    if grid[row][col] == '⬜': 
        return alive_neighbors == 2 or alive_neighbors == 3
    else:  
        return alive_neighbors == 3

def update_grid(grid):
    new_grid = []
    for row in range(len(grid)):
        new_row = []
        for col in range(len(grid[0])):
            if is_alive(grid, row, col):
                new_row.append('⬜')
            else:
                new_row.append('⬛')
        new_grid.append(new_row)
    return new_grid

def save_grid(grid, filename="grid.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for line in grid:
            f.write(' '.join(line) + "\n")

def load_grid(filename="grid.txt"):
    if not os.path.exists(filename):
        return None
    with open(filename, "r", encoding="utf-8") as f:
        grid = [line.strip().split(' ') for line in f]
    return grid

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


if os.path.exists("grid.txt"):
    choice = input("Do you want to load the saved grid? (y/n): ").strip().lower()
    if choice == 'y':
        grid = load_grid()
        rows = len(grid)
        cols = len(grid[0])
    else:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        grid = create_grid(rows, cols)
else:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    grid = create_grid(rows, cols)

while True:
    clear_terminal()
    for line in grid:
        print('\u200A'.join(line))  
    user_input = input("Press Enter to see the next generation or Q to quit: ").strip().lower()
    if user_input == 'q':
        save_grid(grid)
        print("Grid saved. Exiting the program.")
        break
    grid = update_grid(grid)