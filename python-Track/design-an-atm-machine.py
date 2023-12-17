class ATM:

    def __init__(self):
        self.notes_count=[0, 0, 0, 0 ,0]
        self.notes=(20, 50, 100, 200, 500)



    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes_count[i]+=banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        ans=[0,0,0,0,0]
        for i in range(4, -1, -1):
            x=self.notes_count[i]
            if amount>=self.notes[i]:
                y=amount//self.notes[i]
                if x>y:
                    amount%=self.notes[i]
                    ans[i]=y

                else:
                    amount-=(x*self.notes[i])
                    ans[i]=x


        if amount==0:
            for i in range(5):
                self.notes_count[i]-=ans[i] 
            return ans
        else: 
            return [-1]




# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
