# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        def helper(start, end):
            if start >= end:
                return None

            mid = -1
            maxi = -1
            for i in range(start, end):
                if nums[i] > maxi:
                    maxi = nums[i]
                    mid = i
            left = helper(start, mid)
            right = helper(mid+1, end)
            return TreeNode(nums[mid], left, right)

        return helper(0,len(nums))


        