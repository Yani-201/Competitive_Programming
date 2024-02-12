# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # o(1) space implementation ... Floyd's phase 1
        fast=head
        slow=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False

        #o(n) space implementation but solves part1 and part2 together

             

        