class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(cap):
            day, temp = 1, 0
            for num in weights:
                if  temp + num > cap:
                    temp = num
                    day += 1
                else:
                    temp += num
                
            return day <= days

        low, high = max(weights), sum(weights)
        while high >= low:
            mid = low + (high-low)//2
            if check(mid):
                high = mid-1
            else:
                low = mid+1
        return low