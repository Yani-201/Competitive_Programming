class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        i, j, odds, sublength, nice = 0, 0, 0, 0, 0
        while j < len(nums):
            if nums[j]%2 == 1:
                odds += 1
                sublength = 0
            j+=1

            while odds == k:
                if nums[i] % 2 == 1:
                    odds -= 1
                i += 1
                sublength += 1

            nice += sublength

        return nice 

                