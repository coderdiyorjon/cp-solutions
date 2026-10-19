class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n: int = len(nums)
        l: int
        r: int
        l, r = 0, n

        while l < r:
            mid: int = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        ans: list[int] = []

        while l < n and nums[l] == target:
            ans.append(l)
            l += 1

        return ans
