class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        dif=float('inf')

        for k in range(len(nums)-2):

            i=k+1
            j=len(nums)-1
            
            while j>i:
                cur=nums[i]+nums[j]+nums[k]
                if abs(cur-target)<dif:
                    ans=cur
                    dif=abs(cur-target)
                else:
                    if cur-target >= 0:
                        j-=1
                    else:
                        i+=1


        return ans
        