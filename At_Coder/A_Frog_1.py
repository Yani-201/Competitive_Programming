t = int(input())
stones = list(map(int, input().split()))

dp = [0]*t
dp[1] = abs(stones[1] - stones[0])

for i in range(2, t):
    dp[i] = min(dp[i-2]+abs(stones[i] - stones[i-2]), dp[i-1] + abs(stones[i] - stones[i-1]))

print(dp[t-1])

# memo = {}

# def dp(i):
#     if i == 0:
#         return 0
#     if i == 1:
#         memo[i] = abs(stones[i] - stones[i-1])
 
#     if i not in memo:
#         memo[i] = min(dp(i-1) + abs(stones[i]-stones[i-1]), dp(i-2) + abs(stones[i]-stones[i-2]))
#     return memo[i]

# print(dp(t-1))
    













