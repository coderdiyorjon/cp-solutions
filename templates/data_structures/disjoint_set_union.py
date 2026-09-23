"""Disjoint Set Union (Union-Find) Template.

Features:
- Path Compression: Flattens the tree structure during `find`, achieving near O(1) time.
- Union by Size: Attaches the smaller tree to the root of the larger tree.
- Component Tracking: Maintains the sizes of each set and the total number of components.
"""

class DSU:
    def __init__(self, n):
        """Initializes DSU with `n` elements (0 to n - 1).
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        self.parent = list(range(n))
        self.size = [1] * n
        self.components_count = n
        
    def find(self, i):
        """Finds the representative (root) of the set containing `i`.
        Applies path compression for O(alpha(N)) amortized time.
        """
        if self.parent[i] == i:
            return i
        
        # Path compression: point directly to the root
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        """Union the sets containing `i` and `j`.
        
        Returns:
            bool: True if they were merged, False if they were already in the same set.
        Time Complexity: O(alpha(N)) amortized
        """
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            return False  # Already in the same set (cycle detected if building a graph)
        
        # Union by size: attach smaller tree to larger tree
        if self.size[root_i] < self.size[root_j]:
            root_i, root_j = root_j, root_i
        
        self.parent[root_j] = root_i
        self.size[root_i] += self.size[root_j]
        self.components_count -= 1
        
        return True
    
    def get_size(self, i):
        """Returns the size of the set containing element `i`."""
        return self.size[self.find(i)]
    
    def is_connected(self, i, j):
        """Checks if `i` and `j` belong to the same set."""
        return self.find(i) == self.find(j)
