# Intuition

When searching for specific attributes in a dataset, we just need to filter the rows. Since we are looking for products that meet two specific conditions at the exact same time, a simple filtering clause is all that is required.

# Approach

We use a `SELECT` query to retrieve only the `product_id` column from the `Products` table. The core logic happens in the `WHERE` clause. By checking `low_fats = 'Y'` and combining it with `recyclable = 'Y'` using the `AND` operator, we instruct the database engine to return only the rows that satisfy both criteria simultaneously.

# Complexity

* Time complexity:
$O(N)$
Where $N$ is the total number of rows in the `Products` table. The database engine must scan through the records to evaluate the conditions (assuming no compound indexes exist specifically for these columns).
* Space complexity:
$O(1)$
The auxiliary space complexity is constant, as we are only filtering and returning existing data without allocating memory for complex intermediate data structures.

# Code

```postgresql []
-- Write your PostgreSQL query statement below
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';

```
