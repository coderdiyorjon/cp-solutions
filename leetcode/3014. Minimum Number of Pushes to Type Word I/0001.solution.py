class Solution:
    def minimumPushes(self, word: str) -> int:
        # Total number of characters to type
        n = len(word)

        # Current cost (pushes) per character group
        # First 8 chars cost 1 push each, next 8 cost 2, etc.
        i = 1

        # Stores the total number of pushes required
        count = 0

        # Process characters in groups of 8
        while n:
            if n > 8:
                # Take a full group of 8 characters
                # Each character in this group costs 'i' pushes
                count += 8 * i
                n -= 8
            else:
                # Last group (fewer than or equal to 8 characters)
                count += n * i
                n = 0

            # Increase cost for the next group
            i += 1

        return count