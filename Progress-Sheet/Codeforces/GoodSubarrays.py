t = int(input())
from collections import defaultdict
for i in range(t):
    n = int(input())
    tracker = defaultdict(int)
    arr = list(map(int, input()))
    nums = []
    for i in arr:
        nums.append(i - 1)
    
    curr,ans = 0, 0
    tracker[0] = 1
    for i in range(len(nums)):
        curr+=nums[i]
        ans += tracker[curr]
        tracker[curr]+=1
    print(ans)