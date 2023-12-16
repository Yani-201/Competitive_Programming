class UndergroundSystem:

    def __init__(self):
        self.startStation=defaultdict(set)
        self.tracetime=defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startStation[id]=(stationName, t,)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_city = self.startStation[id]
        if (start_city[0], stationName) in self.tracetime:
            self.tracetime[(start_city[0], stationName)][0]+=(t-start_city[1])
            self.tracetime[(start_city[0], stationName)][1]+=1
        else:
            self.tracetime[(start_city[0], stationName)]=[(t-start_city[1]), 1]
            # self.tracetime[(startStation[id][0], stationName)][1]+=1
       

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_sum=self.tracetime[(startStation, endStation)][0]
        total_customer=self.tracetime[(startStation, endStation)][1]

        return total_sum/total_customer
        

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)