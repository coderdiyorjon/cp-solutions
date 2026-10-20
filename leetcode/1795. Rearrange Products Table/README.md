# Intuition

The `Products` table is currently in a "wide" format (pivoted), where each store has its own dedicated column for the price. However, we need the output in a "long" format (unpivoted), where every single availability record (product, store, price) has its own row. To transform columns into rows, we can independently extract the data for each store and then stack those results on top of one another.

# Approach

We can achieve this unpivoting process by writing three separate `SELECT` statements—one for each store column:

1. In the first query, we select the `product_id`, hardcode the string `'store1'` as the `store` column, and grab the value from the `store1` column to serve as the `price`.
2. We add a `WHERE store1 IS NOT NULL` clause so we only extract rows where the product is actually available in that store.
3. We repeat this exact logic for `store2` and `store3`.
4. Finally, we stack the three result sets together using `UNION ALL`. We use `UNION ALL` instead of `UNION` because we know the sets are mutually exclusive (a row represents a unique product-store combination), and `UNION ALL` is faster since it bypasses the overhead of checking for duplicates.

# Complexity

* Time complexity:
$O(N)$
Where $N$ is the total number of rows in the `Products` table. The database engine performs three separate linear scans (or index scans) of the table—one for each `SELECT` statement—and appends the results. $O(3N)$ simplifies to $O(N)$.
* Space complexity:
$O(N)$
The memory required scales linearly with the number of rows outputted. In the worst-case scenario (where every product is available in all three stores), the result set will contain $3N$ rows, which simplifies to $O(N)$ auxiliary space.

# Code

```postgresql []
-- Write your PostgreSQL query statement below
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
WHERE store1 IS NOT null
UNION ALL
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products
WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products
WHERE store3 IS NOT null;

```

