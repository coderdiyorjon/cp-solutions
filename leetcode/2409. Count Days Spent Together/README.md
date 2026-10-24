# 2409. Count Days Spent Together

Alice and Bob are visiting Rome. You are given four strings representing their arrival and departure dates in `"MM-DD"` format. Your task is to calculate the total number of days they spend together in the city. The problem assumes a standard non-leap year (365 days) where the lengths of the months are standard.

---

## Approach 1: Date Simulation & Set Intersection

### Intuition

Instead of manually calculating overlaps month-by-month and worrying about month boundaries, we can map the strings to actual calendar dates. By picking a standard non-leap year (like 2026), we can step through the calendar day-by-day to generate a timeline of their exact stays, and then intersect those timelines.

### Approach

1. **Date Objects:** Convert the `"MM-DD"` strings into `datetime` objects attached to a fixed non-leap year.
2. **Simulation:** Use a `while` loop with a one-day step (`timedelta(days=1)`) to build a list of every specific day Alice is in Rome. Do the exact same for Bob.
3. **Intersection:** Convert both lists into Python sets and use `.intersection()` to find the overlapping days. The length of this intersected set is our answer.

### Complexity

* **Time complexity:** $\mathcal{O}(D_A + D_B)$ where $D$ is the duration of their stays. Bounded by 365 days, this is effectively $\mathcal{O}(1)$.
* **Space complexity:** $\mathcal{O}(D_A + D_B)$ to store the sets, which is strictly bounded by 365 items, simplifying to $\mathcal{O}(1)$.

### Code (`0001.solution.py`)

```python
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        from datetime import datetime, timedelta
        
        M_A, D_A = arriveAlice.split('-')
        start_date_A = datetime(2026, int(M_A), int(D_A))
        M_A, D_A = leaveAlice.split('-')
        end_date_A = datetime(2026, int(M_A), int(D_A))
        
        M_A, D_A = arriveBob.split('-')
        start_date_B = datetime(2026, int(M_A), int(D_A))
        M_A, D_A = leaveBob.split('-')
        end_date_B = datetime(2026, int(M_A), int(D_A))
        
        dates_A = []
        dates_B = []
        
        while start_date_A <= end_date_A:
            dates_A.append(start_date_A)
            start_date_A += timedelta(days=1)
        
        while start_date_B <= end_date_B:
            dates_B.append(start_date_B)
            start_date_B += timedelta(days=1)
        
        return len(set(dates_A).intersection(dates_B))

```

---

## Approach 2: 1D Number Line Intersection (Optimized)

### Intuition

Every date in a non-leap year can be mapped to an absolute integer from 1 to 365. Once we convert the `"MM-DD"` strings into these integers, finding the overlapping days is just a classic 1D line segment intersection problem.

### Approach

1. **Mapping:** Use a hardcoded array of month lengths to build a helper function that converts `"MM-DD"` into the $N$-th day of the year.
2. **Intersection Logic:** The overlap of two intervals $[A_{start}, A_{end}]$ and $[B_{start}, B_{end}]$ always begins at the maximum of their start dates and ends at the minimum of their end dates.
3. **Calculation:** The total overlap is `end - start + 1`. If they don't overlap, `end` will be less than `start`, so we wrap the result in `max(0, result)` to return 0 gracefully.

### Complexity

* **Time complexity:** $\mathcal{O}(1)$ as string splitting, array slicing (max 12 elements), and min/max operations take constant time.
* **Space complexity:** $\mathcal{O}(1)$ since we only use a fixed 12-element array and a few integer variables.

### Code (`0002.solution.py`)

```python
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day(date_str):
            month, day = map(int, date_str.split("-"))
            return sum(days[: month - 1]) + day
            
        start = max(date_to_day(arriveAlice), date_to_day(arriveBob))
        end = min(date_to_day(leaveAlice), date_to_day(leaveBob))
        
        return max(0, end - start + 1)

```