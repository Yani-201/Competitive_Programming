# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse=ListNode()
        temp=head
        while temp:
            new=ListNode(temp.val, reverse)
            reverse=new
            temp=temp.next

        current=head
        while current:
            if current.val!=reverse.val:
                return False
            reverse=reverse.next
            current=current.next
        return True
        