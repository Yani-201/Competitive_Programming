# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.track=defaultdict(int)
        self.maxi = 0

        def count(node):
            if not node:
                return
            else:
                self.track[node.val]+=1
                self.maxi = max(self.track[node.val], self.maxi)
                count(node.left)
                count(node.right)

        count(root)
        ans=[]
        for num in self.track:
            if self.track[num] == self.maxi:
                ans.append(num)
        return ans

        
