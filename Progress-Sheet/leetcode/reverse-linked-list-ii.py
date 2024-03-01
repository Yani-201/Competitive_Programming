# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        start = prev.next
        end = start
        after = None
        for _ in range(right - left + 1):
            temp = start.next
            start.next = after
            after = start
            start = temp

        prev.next = after
        end.next = start
        return dummy.next
