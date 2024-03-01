# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        tracker = defaultdict(list)
        
        def helper(node, col, row):
            if not node:
                return
            
            tracker[col].append((row, node.val))
            helper(node.left, col - 1, row + 1)
            helper(node.right, col + 1, row + 1)
        
        helper(root, 0, 0)
        ans = []
        for col in sorted(tracker):
            values = []
            for r, val in sorted(tracker[col]):
                values.append(val)
            ans.append(values)
            # ans.append([val for _, val in sorted(tracker[col])])
        
        return ans
