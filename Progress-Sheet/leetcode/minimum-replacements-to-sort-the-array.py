class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations=0
        current_max=nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i]>current_max:
                divisions=math.ceil(nums[i]/current_max)
                operations+=divisions-1
                current_max=(nums[i]//divisions)
            else:
                current_max=nums[i]

        return operations

        