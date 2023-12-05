class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        starts, end = min(start, destination) , max(start,destination)
        new_sum=sum(distance[starts:end])
        back_sum=sum(distance)-new_sum
        return min(back_sum, new_sum)