# Intuition

The problem requires us to find the number of distinct leads and distinct partners for every combination of date and car make. Whenever a problem asks for metrics aggregated across specific categories—in this case, grouped by both date and make—it strongly indicates the need for a `GROUP BY` clause. To ensure we only count unique individuals within those groups, we can rely on the `COUNT(DISTINCT ...)` function.

# Approach

1. **Group the Data:** We apply `GROUP BY date_id, make_name` to bundle all rows that share the exact same date and car make into individual partitions.
2. **Calculate Unique Leads:** Within each grouped partition, we apply `COUNT(DISTINCT lead_id)` to count how many unique leads were present. We alias this as `unique_leads`.
3. **Calculate Unique Partners:** Similarly, we apply `COUNT(DISTINCT partner_id)` to count the unique partners within that exact same partition, aliasing it as `unique_partners`.
4. **Selection:** We output the `date_id`, `make_name`, and our two newly calculated aggregate columns.

# Complexity

* Time complexity:
$O(N)$
Where $N$ is the total number of rows in the `DailySales` table. The database engine must perform a full table scan and typically uses a hash map to group the combinations of `date_id` and `make_name` and track the distinct sets in a single pass.
* Space complexity:
$O(U + L + P)$
Where $U$ is the number of unique `(date_id, make_name)` groups, $L$ is the space required to track distinct leads per group, and $P$ is the space required to track distinct partners per group during the aggregation phase.

# Code

```postgresql []
-- Write your PostgreSQL query statement below
SELECT date_id, make_name, COUNT(DISTINCT lead_id) as unique_leads, COUNT(DISTINCT partner_id) as unique_partners
FROM DailySales
GROUP BY date_id, make_name;

```
