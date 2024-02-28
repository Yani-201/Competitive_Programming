# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [[root]]
        def zigzag(path, flag):
            new = []
            if not path:
                return
            
            for i in range(len(path)-1, -1, -1):
                node = path[i]
                if node:
                    if flag:
                        new.append(node.left)
                        new.append(node.right)
                    else:
                        new.append(node.right)
                        new.append(node.left)

            ans.append(new)
            zigzag(new, not flag)
        
        
        zigzag([root], False)
        final = []
        for level in ans:
            temp = []
            for node in level:
                if node:
                    temp.append(node.val)
            if temp:
                final.append(temp)

        return final

        