class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()

        for k in range(len(nums)-2):

            i=k+1
            j=len(nums)-1
            target= -nums[k]

            while j>i:
                if nums[i]+nums[j] == target:
                    ans.add((nums[k], nums[i], nums[j]))
                    i+=1
                    j-=1
                elif nums[i]+nums[j] > target:
                    j-=1
                else:
                    i+=1


        return list(ans)
        