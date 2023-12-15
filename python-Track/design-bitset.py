class Bitset:

    def __init__(self, size: int):
        self.size=size
        self.bits=[0]*self.size
        self.flippedbits=[1]*self.size
        self.countones=0

    def fix(self, idx: int) -> None:
        if self.bits[idx]!=1:
            self.bits[idx]=1
            self.flippedbits[idx]=0
            self.countones+=1
   
    def unfix(self, idx: int) -> None:
        if self.bits[idx]!=0:
            self.bits[idx]=0
            self.flippedbits[idx]=1
            self.countones-=1

    def flip(self) -> None:
        self.bits,self.flippedbits=self.flippedbits,self.bits
        self.countones=self.size-self.countones

    def all(self) -> bool:
        return self.countones==self.size

    def one(self) -> bool:
        return self.countones>=1   

    def count(self) -> int:
        return self.countones

    def toString(self) -> str:
        return "".join([str(i) for i in self.bits])
        
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()