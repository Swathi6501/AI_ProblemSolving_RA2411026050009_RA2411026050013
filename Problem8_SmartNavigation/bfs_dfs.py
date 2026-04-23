from collections import deque

from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in path:   # 🔥 FIX instead of visited set
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


def dfs(graph, start, goal):
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in path:   # 🔥 FIX
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return None