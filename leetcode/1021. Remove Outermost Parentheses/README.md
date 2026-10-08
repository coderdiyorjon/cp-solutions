# Intuition

To remove the outermost parentheses, we first need to identify the boundaries of each "primitive" valid parenthesis string. A valid parenthesis string has an equal number of opening `(` and closing `)` brackets. We can easily track this by using a counter that increments for every open bracket and decrements for every close bracket. Whenever the counter hits zero, we know we have reached the end of one complete primitive block.

# Approach

1. **State Initialization:** Since the string is guaranteed to be a valid parentheses string, the very first character is always `(`. We initialize our `counter` to `1` and our temporary string `primitiveParenthese` to `"("`, effectively "consuming" the first character.
2. **Iteration:** We loop through the string starting from the second character (`s[1:]`).
3. **Tracking Balance:**
* If we see a `(`, we increment the `counter` and add it to our temporary string.
* If we see a `)`, we decrement the `counter` and add it to our temporary string.


4. **Extracting the Core:** When the `counter` reaches `0`, we have successfully isolated a primitive block (e.g., `"(())"`). We slice off the first and last characters using `primitiveParenthese[1:-1]` (leaving just `"()"`) and append it to our result list `res`.
5. **Reset:** We then reset `primitiveParenthese` and `counter` to prepare for the next primitive block in the string.
6. **Final Result:** Finally, we use `''.join(res)` to combine all the stripped blocks into a single string.

# Complexity

* Time complexity:
$O(N)$
We iterate through the string of length $N$ exactly once. While string concatenation and slicing inside the loop take time, they operate on disjoint segments of the original string. Thus, the total time spent building and slicing all primitives sums to $O(N)$. The final `join()` operation also takes $O(N)$.
* Space complexity:
$O(N)$
The list `res` stores the modified strings, and `primitiveParenthese` temporarily holds segments of the string. In the worst case, these auxiliary structures scale linearly with the size of the input string.

# Code

```python []
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = 1
        primitiveParenthese = "("
        res = []
        for char in s[1:]:
            if char == '(':
                counter += 1
                primitiveParenthese += char
            else:
                counter -= 1
                primitiveParenthese += char

                if not counter: 
                    res.append(primitiveParenthese[1: -1])
                    primitiveParenthese = ""
                    counter = 0
        
        return ''.join(res)

```