# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        if k >= length:
            now = 1
            rem = 0
        else:
            now = length // k
            rem = length % k
        
        cur = head
        i = 0
        ans = []
        while cur:
            ans.append(cur)
            for i in range(now-1):
                cur = cur.next
            if rem > 0:
                cur = cur.next
            cur.next, cur  = None, cur.next
            rem -= 1
        
        for l in range(k-len(ans)):
            ans.append(None)
        return ans