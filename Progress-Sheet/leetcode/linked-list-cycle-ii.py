# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # o(1) implementation, Floyd's part1 and 2 together

        fast=head
        slow=head
        flag=False
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                flag=True
                break

        if flag:
            new=head
            while new!=fast:
                new=new.next
                fast=fast.next
            return new

        return None
        
        #o(n) space implementation but solves part1 and part2 together

        # current=head
        # visited=set()
        # visited.add(current)

        # while current:
        #     current=current.next
        #     if current in visited:
        #         return current
        #     visited.add(current)
        # return None
        