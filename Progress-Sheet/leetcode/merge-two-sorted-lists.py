# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(1000)
        current=dummy
   
        while list1 and list2:
            if list2.val>=list1.val:
                current.next=list1
                list1=list1.next 
            else:
                current.next=list2
                list2=list2.next 
            current=current.next

        current.next= list1 or list2
        return dummy.next
        