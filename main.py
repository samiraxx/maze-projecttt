 
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

def create_empty_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def main():
    rows, cols = 10, 10
    maze = create_empty_maze(rows, cols)


    start = (1, 1)
    end = (rows - 2, cols - 2)


    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'

    print("Лабиринт со стартом и финишем:")
    print_maze(maze)

if name == "__main__":
    main()
