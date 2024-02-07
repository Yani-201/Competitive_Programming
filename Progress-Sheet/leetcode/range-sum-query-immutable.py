class NumArray:

    def __init__(self, nums: List[int]):
        self.summ=[nums[0]]
        for i in range(1, len(nums)):
            self.summ.append(nums[i]+self.summ[-1]) 

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.summ[right]
        else:
            return self.summ[right]-self.summ[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)