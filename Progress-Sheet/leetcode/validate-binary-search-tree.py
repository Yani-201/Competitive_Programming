# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversed = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            traversed.append(node.val)
            inorder(node.right)

        inorder(root)
        for i in range(len(traversed)-1):
            if traversed[i] >= traversed[i+1]:
                return False
        return True


        