import random

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    def dfs(x, y):
        dirs = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx < height - 1 and 1 <= ny < width - 1 and maze[nx][ny] == 1:
                maze[nx - dx//2][ny - dy//2] = 0
                maze[nx][ny] = 0
                dfs(nx, ny)
    maze[1][1] = 0
    dfs(1, 1)
    return maze

def solve_maze(maze):
    height, width = len(maze), len(maze[0])
    start, end = (1, 1), (height - 2, width - 2)
    stack = [(*start, [start])]
    visited = set()
    while stack:
        x, y, path = stack.pop()
        if (x, y) == end:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == 0:
                stack.append((nx, ny, path + [(nx, ny)]))
    return None

def print_maze(maze, path=None):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if path and (i, j) in path:
                print('.', end='')
            else:
                print('#' if maze[i][j] == 1 else ' ', end='')
        print()

# Example
maze = generate_maze(21, 21)
path = solve_maze(maze)
print_maze(maze, path)
