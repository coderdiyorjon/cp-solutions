"""Breadth-First Search (BFS) and Depth-First Search (DFS) Templates.

Includes:
1. Standard BFS (Shortest path in unweighted graphs)
2. Standard DFS (Iterative and Recursive)
3. 2D Grid BFS/DFS patterns (using dx, dy direction arrays)
"""

import sys
from collections import deque

# Increase recursion depth for deep trees/graphs in Python
sys.setrecursionlimit(200000)

# ---------------------------------------------------------
# 1. Adjacency List Traversals
# ---------------------------------------------------------

def bfs_shortest_path(graph, start):
    """Finds the shortest path from start to all other nodes in an unweighted graph.
    
    Args:
        graph: List of lists or dict representing adjacency list.
        start: Starting node.
        
    Returns:
        distances: Dictionary mapping node to its shortest distance from start.
    """
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances


def dfs_recursive(graph, node, visited):
    """Explores the graph completely starting from `node`.
    
    Args:
        graph: Adjacency list.
        node: Current node.
        visited: Set of visited nodes to prevent cycles.
    """
    visited.add(node)
    
    # Process node here (e.g., add to a component list)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# ---------------------------------------------------------
# 2. 2D Grid Traversals (Matrices)
# ---------------------------------------------------------

# Directions: Right, Down, Left, Up (can add diagonals if needed)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(r, c, rows, cols):
    """Checks if the coordinate is within grid bounds."""
    return 0 <= r < rows and 0 <= c < cols


def bfs_grid(grid, start_r, start_c):
    """Traverses a 2D grid using BFS.
    Useful for finding the shortest path out of a maze.
    """
    rows, cols = len(grid), len(grid[0])
    visited = set([(start_r, start_c)])
    queue = deque([(start_r, start_c, 0)]) # (row, col, distances)
    
    while queue:
        r, c, dist = queue.popleft()
        
        # Check all 4 adjacent directions
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            
            # Add custom conditions here (e.g., grid[nr][nc] != 'obstacle')
            if is_valid(nr, nc, rows, cols) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return visited
