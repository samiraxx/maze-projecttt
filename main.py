ROWS = 10
COLS = 10
WALL = '#'
PATH = ' '

maze = [[WALL for _ in range(COLS)] for _ in range(ROWS)]

def print_maze():
    for row in maze:
        print(''.join(row))

print_maze()
