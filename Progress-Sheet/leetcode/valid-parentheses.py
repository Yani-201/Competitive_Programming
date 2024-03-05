class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        tracker = {')': '(', ']': '[', '}': '{'}

        for i in range(len(s)):
            if s[i] not in tracker:
                stack.append(s[i])
            else:
                if len(stack)!= 0 and (stack[-1] == tracker[s[i]]):
                    stack.pop()
                else: 
                    return False
        return True if len(stack)==0 else False
        