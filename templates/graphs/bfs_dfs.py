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

def bfs_shortest_path(graph: list[list[int]] | dict[int, list[int]], start: int) -> dict[int, int]:
    """Finds the shortest path from start to all other nodes in an unweighted graph.
    
    Args:
        graph: List of lists or dict representing adjacency list.
        start: Starting node.
        
    Returns:
        distances: Dictionary mapping node to its shortest distance from start.
    """
    distances: dict[int, int] = {start: 0}
    queue: deque[int] = deque([start])
    
    while queue:
        node: int = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances


def dfs_recursive(graph: list[list[int]] | dict[int, list[int]], node: int, visited: set[int]) -> None:
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
DIRECTIONS: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(r: int, c: int, rows: int, cols: int) -> bool:
    """Checks if the coordinate is within grid bounds."""
    return 0 <= r < rows and 0 <= c < cols


def bfs_grid(grid: list[list[str | int]], start_r: int, start_c: int) -> set[tuple[int, int]]:
    """Traverses a 2D grid using BFS.
    Useful for finding the shortest path out of a maze.
    """
    rows: int = len(grid)
    cols: int = len(grid[0])
    visited: set[tuple[int, int]] = set([(start_r, start_c)])
    queue: deque[tuple[int, int, int]] = deque([(start_r, start_c, 0)]) # (row, col, distances)
    
    while queue:
        
        r: int
        c: int
        dist: int
        r, c, dist = queue.popleft()
        
        # Check all 4 adjacent directions
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            
            # Add custom conditions here (e.g., grid[nr][nc] != 'obstacle')
            if is_valid(nr, nc, rows, cols) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return visited
