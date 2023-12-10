class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        pivot_n=0

        for i in nums:
            if i>pivot:
                right.append(i)
            elif i<pivot:
                left.append(i)
            else:
                pivot_n+=1

        for j in range(pivot_n):
            left.append(pivot)
            
        return left + right