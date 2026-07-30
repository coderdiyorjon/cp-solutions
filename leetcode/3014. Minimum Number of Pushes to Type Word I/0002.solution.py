class Solution:
    def minimumPushes(self, word: str) -> int:
        # Number of characters that need to be typed
        n = len(word)

        # Characters are assigned costs in groups of 8:
        # indices 0-7   -> 1 push each
        # indices 8-15  -> 2 pushes each
        # indices 16-23 -> 3 pushes each
        # indices 24-31 -> 4 pushes each
        #
        # For a character at position i,
        # i // 8 gives its group number (0, 1, 2, 3),
        # so i // 8 + 1 gives its push cost.
        return sum((i // 8 + 1) for i in range(n))