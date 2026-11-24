class Solution:
    def maxLength(self, nums: list[int]) -> int:
        # Prime factors for each number from 0 to 10
        PRIMES = (
            (),      # 0 (unused)
            (),      # 1 (no prime factors)
            (2,),    # 2
            (3,),    # 3
            (2,),    # 4
            (5,),    # 5
            (2, 3),  # 6
            (7,),    # 7
            (2,),    # 8
            (3,),    # 9
            (2, 5),  # 10
        )

        last_seen = [-1] * 8
        res = min(len(nums), 2)
        start = 0

        for end, x in enumerate(nums):
            for p in PRIMES[x]:
                if last_seen[p] >= start:
                    start = last_seen[p] + 1
                last_seen[p] = end

            curr_len = end - start + 1
            if curr_len > res:
                res = curr_len

        return res
