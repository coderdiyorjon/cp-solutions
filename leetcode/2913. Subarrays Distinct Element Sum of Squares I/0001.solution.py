class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        total_sum: int
        total_sum = 0
        array_length: int
        array_length = len(nums)

        for i in range(array_length):
            distinct_elements: set[int]
            distinct_elements = set()
            
            for j in range(i, array_length):
                distinct_elements.add(nums[j])
                
                distinct_counts: int
                distinct_counts = len(distinct_elements)
                
                total_sum += distinct_counts ** 2
            
        return total_sum