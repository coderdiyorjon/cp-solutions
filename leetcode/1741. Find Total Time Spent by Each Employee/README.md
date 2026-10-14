# Intuition

To find the total time an employee spends in the office on a specific day, we need to account for the fact that they might enter and leave multiple times. The duration of each individual visit is simply the difference between the time they leave and the time they arrive. By grouping the records by both the day and the employee, we can sum these individual durations to get the total daily time.

# Approach

1. **Calculate Individual Durations:** For every row in the table, subtract `in_time` from `out_time` to find the duration of that specific office visit.
2. **Aggregate by Day and Employee:** Use the `SUM()` function to add all these individual durations together.
3. **Group the Data:** Apply a `GROUP BY` clause on `event_day` and `emp_id`. This ensures the sum is calculated strictly for each unique employee on each specific date.
4. **Format Output:** Select the required columns, making sure to alias `event_day` as `day` and the summed duration as `total_time` to match the expected result schema.

# Complexity

* Time complexity:
$O(N)$
Where $N$ is the total number of rows in the `Employees` table. The database engine scans the table to compute the time differences and groups the records (typically using hash aggregation) in linear time.
* Space complexity:
$O(U)$
Where $U$ is the number of unique `(event_day, emp_id)` pairs. This represents the memory used by the database to store the intermediate grouping states before returning the final output.

# Code

```postgresql []
-- Write your PostgreSQL query statement below
SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;

```
