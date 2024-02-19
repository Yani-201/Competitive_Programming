# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-10000)
        dummy.next = head
        current = head.next
        prev = head

        while current:
            if current: nex = current.next 
            else: return dummy.next
            prev.next = nex

            newNode = ListNode(current.val)
            temp = dummy
            now = dummy.next
            while temp and now:
                if now.val >= newNode.val: break
                temp = now
                now = now.next

            newNode.next = now
            temp.next = newNode
            
            if newNode == prev.next: prev =  prev.next
            current = nex

        return dummy.next
