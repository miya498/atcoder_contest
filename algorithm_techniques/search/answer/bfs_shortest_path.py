from collections import deque

def shortest_path(graph, start, target):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        node, distance = queue.popleft()
        if node == target:
            return distance
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1

# 使用例
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("Shortest path length:", shortest_path(graph, 'A', 'F'))