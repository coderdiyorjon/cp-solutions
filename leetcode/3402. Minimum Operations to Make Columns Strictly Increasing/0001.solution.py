from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        # Initialize the total number of operations required
        oper_count = 0
        
        # Iterate over each column index 'j'
        for j in range(len(grid[0])):
            # Iterate downwards row by row, stopping at the second-to-last row
            for i in range(len(grid) - 1):
                # If the current element is greater than or equal to the element directly below it
                if grid[i][j] >= grid[i + 1][j]:
                    # To be strictly increasing, the element below MUST be at least current + 1
                    target = grid[i][j] + 1
                    
                    # Add the exact difference to our total operations count
                    oper_count += target - grid[i + 1][j]
                    
                    # Update the grid in-place to reflect this required operation 
                    # so the next row down compares against the correct new baseline
                    grid[i + 1][j] = target
                    
        return oper_count
