def solve_maze(maze):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1

    def get_neighbors(x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    start = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                start = (i, j)
                break
        if start:
            break

    stack = [start]
    visited = set()
    parent = {}

    while stack:
        x, y = stack.pop()
        
        if maze[x][y] == 3:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]
        
        if (x, y) not in visited:
            visited.add((x, y))
            for nx, ny in get_neighbors(x, y):
                if is_valid(nx, ny) and (nx, ny) not in visited:
                    stack.append((nx, ny))
                    parent[(nx, ny)] = (x, y)
    
    return None  


maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 3],
    [2, 1, 0, 0, 0]
]

path = solve_maze(maze)
if path:
    print("Path found:", path)
else:
    print("No path found")


def print_maze_with_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print("*", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

print("\nMaze with path:")
print_maze_with_path(maze, path)
