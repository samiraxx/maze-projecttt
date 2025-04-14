 
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
import random

def create_empty_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def generate_maze(maze, x, y):
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 1 <= nx < len(maze)-1 and 1 <= ny < len(maze[0])-1:
            if maze[nx][ny] == '#':
                maze[nx - dx // 2][ny - dy // 2] = ' '
                maze[nx][ny] = ' '
                generate_maze(maze, nx, ny)

def main():
    rows, cols = 11, 11 
    maze = create_empty_maze(rows, cols)


    start_x, start_y = 1, 1
    maze[start_x][start_y] = ' '

 
    generate_maze(maze, start_x, start_y)

    print("Сгенерированный лабиринт:")
    print_maze(maze)

if name == "__main__":
    main()
import random

def create_empty_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def generate_maze(maze, x, y):
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 1 <= nx < len(maze)-1 and 1 <= ny < len(maze[0])-1:
            if maze[nx][ny] == '#':
                maze[nx - dx // 2][ny - dy // 2] = ' '
                maze[nx][ny] = ' '
                generate_maze(maze, nx, ny)

def add_start_and_finish(maze):
    maze[1][1] = 'S'  
    maze[-2][-2] = 'F'  

def main():
    rows, cols = 11, 11
    maze = create_empty_maze(rows, cols)

    start_x, start_y = 1, 1
    maze[start_x][start_y] = ' '

    generate_maze(maze, start_x, start_y)

    add_start_and_finish(maze)

    print("Лабиринт со стартом и финишем:")
    print_maze(maze)

if name == "__main__":
    main()
    import random

def create_empty_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def generate_maze(maze, x, y):
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 1 <= nx < len(maze)-1 and 1 <= ny < len(maze[0])-1:
            if maze[nx][ny] == '#':
                maze[nx - dx // 2][ny - dy // 2] = ' '
                maze[nx][ny] = ' '
                generate_maze(maze, nx, ny)

def add_start_and_finish(maze):
    maze[1][1] = 'S'
    maze[-2][-2] = 'F'

def find_path(maze, x, y):
    if maze[x][y] == 'F':
        return True

    if maze[x][y] != ' ' and maze[x][y] != 'S':
        return False

    if maze[x][y] != 'S':
        maze[x][y] = '.'

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if find_path(maze, nx, ny):
            return True

    if maze[x][y] != 'S':
        maze[x][y] = ' '
    return False

def main():
    rows, cols = 11, 11
    maze = create_empty_maze(rows, cols)

    start_x, start_y = 1, 1
    maze[start_x][start_y] = ' '

    generate_maze(maze, start_x, start_y)
    add_start_and_finish(maze)

    find_path(maze, start_x, start_y)

    print("Лабиринт с найденным путём:")
    print_maze(maze)

if name == "__main__":
    main()
    def find_path(maze, start, end, path=[]):
    x, y = start
    if start == end:  
        return path + [start]
    
    
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] == 1:
        return None

  

   
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        new_path = find_path(maze, (new_x, new_y), end, path + [(x, y)])
        if new_path:
            return new_path

    return None 