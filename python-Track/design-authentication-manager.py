class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.timer=defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.timer[tokenId]=(currentTime+self.timeToLive)   

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.timer[tokenId]>currentTime:
            self.timer[tokenId]=(currentTime+self.timeToLive)
        else: del self.timer[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ct=0
        for i in self.timer:
            if self.timer[i]>currentTime:
                ct+=1

        return ct
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)