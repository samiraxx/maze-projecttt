 
def create_empty_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def main():
    rows, cols = 10, 10
    maze = create_empty_maze(rows, cols)
    print("Пустой лабиринт:")
    print_maze(maze)

if name == "__main__":
    main()
