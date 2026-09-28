class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mx tracks the maximum depth we've seen so far.
        # count tracks our current depth as we read the string.
        Mx = count = 0
        
        # Iterate through every character in the string
        for char in s:
            if char == '(':
                # An opening bracket means we go one level deeper
                count += 1
                # Update Mx if our current depth is the deepest we've been
                Mx = Mx if Mx > count else count
                
            elif char == ')':
                # A closing bracket means we step back out one level
                count -= 1
        
        # Return the maximum depth recorded
        return Mx
