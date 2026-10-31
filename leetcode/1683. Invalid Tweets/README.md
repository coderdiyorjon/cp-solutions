# Intuition

In database design and backend validation, enforcing character limits on text fields is a fundamental requirement. To identify entries that violate these rules, we simply need a function that maps the text payload to its scalar integer length. Any row where this scalar value strictly exceeds the defined threshold is considered invalid.

# Approach

We use a standard `SELECT` statement to retrieve only the `tweet_id`. The filtering logic is handled in the `WHERE` clause using PostgreSQL's built-in `LENGTH()` function. This function evaluates the character count of the `content` string for each row. By applying the logical condition `LENGTH(content) > 15`, the database engine filters out any tweets that fit within the allowed limit, leaving only the invalid ones.

# Complexity

* Time complexity:
$\mathcal{O}(N)$
Where $N$ is the number of rows in the `Tweets` table. The database engine must perform a linear scan, reading the `content` column of each row to compute its length and evaluate the condition.
* Space complexity:
$\mathcal{O}(1)$
The auxiliary space required for the operation is constant, as the filtering is evaluated row by row without allocating memory for complex intermediate data structures.

# Code

```postgresql []
-- Write your PostgreSQL query statement below
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;

```

