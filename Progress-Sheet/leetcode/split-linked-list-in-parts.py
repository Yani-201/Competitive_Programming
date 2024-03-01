# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [[] for _ in range(k)] 

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        cap = length // k
        rem = length % k
        idx = 0
        cur = head
        while cur:
            if len(ans[idx]) < cap:
                ans[idx].append(cur.val)
            elif len(ans[idx]) == cap:
                if rem > 0:
                    ans[idx].append(cur.val)
                    rem -= 1
                    idx += 1
                else:
                    idx+=1
                    ans[idx].append(cur.val)
            else:
                idx += 1
            cur = cur.next

        splitted = []
        for nodes in ans:
            dummy = ListNode()
            current = dummy
            for val in nodes:
                temp = ListNode(val)
                current.next = temp
                current = current.next
            splitted.append(dummy.next)
        # print(ans)

        return splitted
        