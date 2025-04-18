import random

ROWS = 21
COLS = 21
WALL = '#'
PATH = ' '
VISITED = '.'

maze = [[WALL for _ in range(COLS)] for _ in range(ROWS)]

directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def is_valid(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def generate_maze(r, c):
    maze[r][c] = PATH
    random.shuffle(directions)
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc) and maze[nr][nc] == WALL:
            maze[r + dr // 2][c + dc // 2] = PATH
            generate_maze(nr, nc)

def find_path(r, c):
    if not is_valid(r, c) or maze[r][c] != PATH:
        return False
    if (r, c) == (ROWS - 2, COLS - 2):
        maze[r][c] = VISITED
        return True
    maze[r][c] = VISITED
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if find_path(r + dr, c + dc):
            return True
    maze[r][c] = PATH
    return False

def print_maze():
    for row in maze:
        print(''.join(row))

generate_maze(1,1)
maze[1][1] = PATH
maze[ROWS - 2][COLS - 2] = PATH
find_path(1, 1)
print_maze()
