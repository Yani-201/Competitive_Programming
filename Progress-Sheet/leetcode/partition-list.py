# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummybefore = ListNode(-1000)
        dummyafter = ListNode(1000)

        before = dummybefore
        after = dummyafter

        current = head
        while current:
            newNode = ListNode(current.val)
            if current.val < x:
                before.next = newNode
                before = before.next

            else:
                after.next = newNode
                after = after.next

            current=current.next

        before.next = dummyafter.next

        return dummybefore.next

        