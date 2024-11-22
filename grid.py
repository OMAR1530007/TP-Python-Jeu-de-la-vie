import random

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