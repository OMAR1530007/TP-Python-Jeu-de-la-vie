import os

def save_grid(grid_history, filename="grid_save.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for grid in grid_history:
            for line in grid:
                f.write(' '.join(line) + "\n")
            f.write("\n") 

def load_grid(filename="grid_save.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        grids = f.read().strip().split("\n\n")
        grid_history = []
        for grid in grids:
            grid_history.append([line.split(' ') for line in grid.split("\n")])
    return grid_history