# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(1)
        dummy.next=head
        current=dummy
        while current and n>=0:
            current=current.next
            n-=1

        back=dummy
        while current:
            current=current.next
            back=back.next

        if back.next:
            back.next=back.next.next

        return dummy.next
