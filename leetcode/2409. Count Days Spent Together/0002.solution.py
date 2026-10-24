class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day(date_str):
            month, day = map(int, date_str.split("-"))
            return sum(days[: month - 1]) + day
            
        start = max(date_to_day(arriveAlice), date_to_day(arriveBob))
        end = min(date_to_day(leaveAlice), date_to_day(leaveBob))
        
        return max(0, end - start + 1)