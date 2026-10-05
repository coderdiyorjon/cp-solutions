# 2356. Number of Unique Subjects Taught by Each Teacher

You are given a `Teacher` table containing information about teachers, the subjects they teach, and the departments they belong to.

Your task is to write a SQL query to report the number of unique subjects each teacher teaches in the university. The result table can be returned in any order.

---

## Schema

**Table: `Teacher`**

| Column Name | Type |
| --- | --- |
| teacher_id | int |
| subject_id | int |
| dept_id | int |

*(subject_id, dept_id) is the primary key for this table. Each row in this table indicates that the teacher with `teacher_id` teaches the subject `subject_id` in the department `dept_id`.*

---

## Example

**Input:**

`Teacher` table:

| teacher_id | subject_id | dept_id |
| --- | --- | --- |
| 1 | 2 | 3 |
| 1 | 2 | 4 |
| 1 | 3 | 3 |
| 2 | 1 | 1 |
| 2 | 2 | 1 |
| 2 | 3 | 1 |
| 2 | 4 | 1 |

**Output:**

| teacher_id | cnt |
| --- | --- |
| 1 | 2 |
| 2 | 4 |

**Explanation:**

* Teacher 1 teaches subject 2 in departments 3 and 4, and subject 3 in department 3. The unique subjects taught are 2 and 3 (total of 2).
* Teacher 2 teaches subjects 1, 2, 3, and 4 in department 1. The unique subjects taught are 1, 2, 3, and 4 (total of 4).

---

## Intuition

This is a classic relational database aggregation problem. We need to look at data on a *per-teacher* basis.

Whenever a problem asks for a metric "for each [entity]," it is a direct indicator that a `GROUP BY` clause is required on that entity's identifier.

Since a teacher might teach the exact same subject across multiple different departments (creating multiple rows for the same subject), simply using `COUNT(subject_id)` would lead to overcounting. To filter out these duplicates and count only the unique subjects, we apply the `DISTINCT` keyword inside the `COUNT()` aggregate function.

---

## Solution: PostgreSQL Aggregation

### Idea

1. Group the dataset by `teacher_id` to isolate records for each individual instructor.
2. Apply `COUNT(DISTINCT subject_id)` to calculate the number of unique subjects per group.
3. Alias the aggregated column as `cnt` to satisfy the requested output format.

### Implementation

```postgresql
SELECT 
    teacher_id, 
    COUNT(DISTINCT subject_id) AS cnt
FROM 
    Teacher
GROUP BY 
    teacher_id;

```

### Complexity Analysis

* **Time Complexity:** O(N) or O(N log N) depending on the database engine's internal implementation of the `GROUP BY` operation (often utilizing hashing or sorting over the `N` rows in the table).
* **Space Complexity:** O(U) where U is the number of unique `teacher_id` values stored in the intermediate hash table or sort buffer during the aggregation phase.