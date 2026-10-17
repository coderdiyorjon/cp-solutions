# Intuition

To report the product name alongside its sales year and price, we need to pull information from two separate tables. The `Sales` table contains the transactional data (`year`, `price`), while the `Product` table holds the descriptive data (`product_name`). Since both tables share the `product_id` column, an `INNER JOIN` is the perfect tool to merge them and extract the required fields.

# Approach

We use a standard `JOIN` (which defaults to an `INNER JOIN` in PostgreSQL) to combine the `Sales` and `Product` tables. The `ON` clause specifies that the tables should be linked where their `product_id` values match. Finally, the `SELECT` statement filters the output to only return the exact three columns requested: `product_name`, `year`, and `price`.

# Complexity

* Time complexity:
$O(N \log M)$ or $O(N + M)$
The exact time complexity depends on the database engine's query execution plan (e.g., Hash Join vs. Nested Loop Join). Generally, it scales with the size of the `Sales` table ($N$) and the `Product` table ($M$).
* Space complexity:
$O(N)$
The space complexity corresponds to the memory required to hold the final result set, which will be proportional to the number of rows in the `Sales` table.

# Code

```postgresql []
-- Write your PostgreSQL query statement below
SELECT product_name, year, price
FROM Sales JOIN Product ON Sales.product_id = Product.product_id;

```
