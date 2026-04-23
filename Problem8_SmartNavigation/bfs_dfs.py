from collections import deque

# BFS Algorithm
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None


# DFS Algorithm
def dfs(graph, start, goal):
    visited = set()
    stack = [[start]]
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    
    return None