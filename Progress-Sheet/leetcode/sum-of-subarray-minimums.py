class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        # prefix iteration
        stack = []
        pref = [1]* len(arr)
        for i,num in enumerate(arr):
            temp = 1
            while len(stack) > 0 and stack[-1][0] >= num:
                temp += stack.pop()[1]
            stack.append((num, temp))
            pref[i] = temp

        # suffix iteration
        stack = []
        suff = [1] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            temp = 1
            while len(stack) > 0 and stack[-1][0] > arr[i]:
                temp += stack.pop()[1]
            stack.append((arr[i], temp))
            suff[i] = temp 

        # answer calc
        ans = 0
        for i in range(len(pref)):
            ans += pref[i] * suff[i] * arr[i]

        return ans % ((10**9)+7)


# // Trying to do it in one iteration

# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         stack = []
#         MOD =  10 ** 9 + 7
#         res = 0

#         for i, num in enumerate(arr):
            
#             while stack and stack[-1][0] > num:
#                 n, j = stack.pop()
#                 left = j - stack[-1][1] if stack else j + 1
#                 right = i - j

#                 res = (res + left * right * n) % MOD

#             stack.append([num, i])    

#         while stack:
#             n, j = stack.pop()
#             left = j - stack[-1][1] if stack else j + 1
#             right = len(arr) - j

#             res = (res + left * right * n) % MOD
        
#         return res

        