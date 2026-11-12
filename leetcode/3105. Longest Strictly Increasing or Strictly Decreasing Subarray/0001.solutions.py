class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inf = float('inf')
        def increasing(nums: list[int]) -> int:
            length: int = 0
            longest: int = 0
            prev: float = inf

            for num in nums:
                if num > prev:
                    length += 1
                else:
                    length = 1
                prev = num
                longest = length if length > longest else longest
            
            return longest
        return max(increasing(nums), increasing([-num for num in nums]))
