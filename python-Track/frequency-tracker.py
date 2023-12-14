class FrequencyTracker:

    def __init__(self):
        self.freq=defaultdict(int)
        self.freq2 =defaultdict(int)

    def add(self, number: int) -> None:
        self.freq2[self.freq[number]]-=1
        self.freq[number]+=1
        self.freq2[self.freq[number]]+=1

    def deleteOne(self, number: int) -> None:
        if self.freq and number in self.freq and self.freq[number]!=0:
            self.freq2[self.freq[number]]-=1
            self.freq[number]-=1
            self.freq2[self.freq[number]]+=1


    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq2 and self.freq2[frequency]!=0:
            return True 
        return False 



        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)