class Solution(object):
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n: int = len(nums)
        ans: list[list[int]] = []
        sol: list[int] = []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return ans
