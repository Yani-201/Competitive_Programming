# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        visited=set()
        visited.add(current)

        while current:
            current=current.next
            if current in visited:
                return current
            visited.add(current)
        return None
        