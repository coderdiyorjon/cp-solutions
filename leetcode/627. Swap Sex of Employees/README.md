# Intuition

To modify existing records in a database rather than simply retrieving them, we must use a Data Manipulation Language (DML) command, specifically the `UPDATE` statement. The challenge here is swapping values in a single pass. If we sequentially updated 'f' to 'm' and then 'm' to 'f' in two separate statements, the first statement would overwrite all the original females to males, and the second statement would immediately flip the entire table to female. To prevent this data loss, we need atomic, row-level conditional logic.

# Approach

We use an `UPDATE` statement targeting the `Salary` table. To handle the conditional swapping in a single pass, we assign the `sex` column to the result of a `CASE` expression.

The `CASE` expression evaluates each row individually:

1. `WHEN sex = 'f' THEN 'm'`: If the current value is female, flip it to male.
2. `ELSE 'f'`: Since the problem guarantees the values are exclusively 'm' or 'f', any row that didn't match 'f' must be 'm', so we safely default it to 'f'.

# Complexity

* Time complexity:
$\mathcal{O}(N)$
Where $N$ is the total number of rows in the `Salary` table. The database engine must perform a full table scan and evaluate the `CASE` condition for every single row.
* Space complexity:
$\mathcal{O}(1)$
The update is performed in-place. No additional tables or significant memory buffers are required to execute this conditional swap.

# Code

```postgresql []
-- Write your PostgreSQL query statement below
UPDATE Salary
SET sex = CASE
    WHEN sex = 'f' THEN 'm'
    ELSE 'f'
END;

```

