class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        seats=[0]*1000
        for trip in trips:
            seats[trip[1]]+=trip[0]
            if trip[2]<1000:
                seats[trip[2]]-=trip[0]
        _maxi=seats[0]
        for i in range(1,len(seats)):
            seats[i]+=seats[i-1]
            _maxi=max(_maxi, seats[i])
        return capacity>=_maxi

       