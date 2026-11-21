
# Intuition

Building explicit Binary Search Tree (BST) node structures with pointers isn't strictly necessary just to compare whether two trees have the same shape. In any BST, the first inserted element is always the root. Every subsequent element smaller than the root belongs to the left subtree, and every element larger belongs to the right subtree—maintaining their exact relative insertion order. By recursively partitioning two insertion sequences around their roots, we can check structural equivalence directly on the lists. ```https://icpc.kattis.com/problems/ceiling```

# Approach

1. **Recursive Shape Comparison (`same_or_not`):**
* **Base Cases:** If the two sequences have different lengths, their subtrees cannot have the same shape (`False`). If both have length at most 1 (empty or a single node), they are guaranteed to match (`True`).
* **Partitioning:** Treat `a[0]` and `b[0]` as the roots. Iterate through the remaining elements, splitting each list into left (`al`, `bl`) and right (`ar`, `br`) sublists based on whether each value is smaller or larger than its respective root.
* **Recursion:** Return `True` only if both the left subtrees match and the right subtrees match.


2. **Deduplication:** Maintain a list `trees` of unique BST sequences encountered so far. For each new input sequence `nums`, compare it against every stored sequence in `trees`.
3. **Python `for ... else` Pattern:** If a match is found, `break` out of the loop. If the loop completes without hitting `break` (meaning no existing tree shares this shape), the `else` block triggers—incrementing `counts` and appending `nums` to `trees`.

# Complexity

* Time complexity:
$\mathcal{O}(N^2 K^2)$
Comparing two sequences of length $K$ takes $\mathcal{O}(K^2)$ in the worst case (when the BST is completely skewed, such as sorted input, causing $K + (K-1) + \dots + 1$ partitioning steps). In the worst case where all $N$ prototypes are unique, each new sequence is compared against up to $N$ previous ones, giving $\mathcal{O}(N^2 K^2)$. With $N \le 50$ and $K \le 20$, this runs well within the time limit.
* Space complexity:
$\mathcal{O}(N \cdot K + K^2)$
Storing up to $N$ unique sequences of length $K$ requires $\mathcal{O}(N \cdot K)$ space. During `same_or_not`, the recursion depth and temporary partition lists can reach $\mathcal{O}(K^2)$ space in the worst-case skewed tree.

# Code

```python
def same_or_not(a, b):
    if len(a) != len(b):
        return False
    if len(a) <= 1:
        return True

    al, ar = [], []
    bl, br = [], []

    for i in range(1, len(a)):
        if a[i] < a[0]:
            al.append(a[i])
        else:
            ar.append(a[i])

        if b[i] < b[0]:
            bl.append(b[i])
        else:
            br.append(b[i])

    return same_or_not(al, bl) and same_or_not(ar, br)


N, K = map(int, input().strip().split())
trees = []
counts = 0

for _ in range(N):
    nums = list(map(int, input().strip().split()))

    for t in trees:
        if same_or_not(nums, t):
            break
    else:
        # Runs only if no matching tree shape was found
        counts += 1
        trees.append(nums)

print(counts)

```