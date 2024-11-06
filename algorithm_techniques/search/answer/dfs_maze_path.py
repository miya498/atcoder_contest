def has_path(maze, start, destination):
    def dfs(x, y):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] == 1:
            return False
        if (x, y) == destination:
            return True
        maze[x][y] = 1
        return (dfs(x + 1, y) or dfs(x - 1, y) or dfs(x, y + 1) or dfs(x, y - 1))

    return dfs(start[0], start[1])

# 使用例
if __name__ == "__main__":
    maze = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    start, destination = (0, 0), (3, 3)
    print("Path exists:", has_path(maze, start, destination))
