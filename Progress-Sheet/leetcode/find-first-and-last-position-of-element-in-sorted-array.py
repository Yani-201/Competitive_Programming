class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] >= target:
                r = mid  -1
            else:
                l = mid + 1
        low = -1 if (l >= len(nums) or nums[l] != target) else l
        if low == -1:
            return [-1,-1]
        l,r = low, len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                l = mid +1
            else:
                r = mid -1
        return [low, r]

