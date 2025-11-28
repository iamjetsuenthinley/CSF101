from collections import deque

def solve_maze_bfs(maze):
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

    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        x, y = queue.popleft()
        
        if maze[x][y] == 3:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]
        
        for nx, ny in get_neighbors(x, y):
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
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

path = solve_maze_bfs(maze)
if path:
    print("Shortest path found:", path)
    print("Path length:", len(path) - 1)
    print("No path found")

def print_maze_with_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print("*", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

print("\nMaze with shortest path:")
print_maze_with_path(maze, path)
