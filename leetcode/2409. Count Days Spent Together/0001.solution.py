class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        from datetime import datetime, timedelta
        
        M_A: str
        D_A: str
        start_date_A: object
        end_date_A: object
        start_date_B: object
        end_date_B: object

        M_A, D_A = arriveAlice.split('-')
        start_date_A = datetime(2026, int(M_A), int(D_A))
        M_A, D_A = leaveAlice.split('-')
        end_date_A = datetime(2026, int(M_A), int(D_A))
        
        M_A, D_A = arriveBob.split('-')
        start_date_B = datetime(2026, int(M_A), int(D_A))
        M_A, D_A = leaveBob.split('-')
        end_date_B = datetime(2026, int(M_A), int(D_A))
        
        dates_A: list[object] = []
        dates_B: list[object] = []
        
        while start_date_A <= end_date_A:
            dates_A.append(start_date_A)
            start_date_A += timedelta(days=1)
        
        while start_date_B <= end_date_B:
            dates_B.append(start_date_B)
            start_date_B += timedelta(days=1)
        
        return len(set(dates_A).intersection(dates_B))