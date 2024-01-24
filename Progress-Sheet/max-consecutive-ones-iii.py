class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        le=0
        while j<len(nums):
            if nums[j]==0:
                if k>0:
                    k-=1
                    j+=1
                else:
                    le=max(le, j-i)
                    if nums[i]==0:
                        k+=1
                        i+=1
                    else:
                        i+=1        
                
            else:
                j+=1
            
        
        return max(le,j-i)