class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        start , end = points[0]

        for i in range(1, len(points)):
            cur_start, cur_end = points[i] 

            start=max(cur_start, start)  
            end=min(cur_end, end)  

            if end < start:
                start = cur_start
                end = cur_end
                count += 1

        return count
