class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        # /// without using concept of queue
        res = 0
        for i, num in enumerate(tickets):
            if i <= k:
                if num < tickets[k]:
                    res += num
                else:
                    res += tickets[k]
            else:
                if num <= tickets[k]-1:
                    res += num
                else:
                    res += tickets[k]-1

        return res


# # with using queue
#         que = deque(tickets)
#         time = 0
#         while que[k] > 1 or k !=0:
#             temp = que.popleft() -1 
#             if temp > 0:
#                 que.append(temp)
#             k -= 1
#             if k < 0:
#                 k = len(que)-1
#             time +=1
#         return time+1

        