# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current=head
        visited=set()
        visited.add(current)

        while current:
            current=current.next
            if current in visited:
                return True
            visited.add(current)
        return False
             

        