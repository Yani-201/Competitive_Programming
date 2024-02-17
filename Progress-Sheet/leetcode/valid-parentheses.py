class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            if i == "(" or i =="{" or i=="[":
                stack.append(i)
            else:
                if len(stack)!= 0 and ((i == ")" and stack[-1] == "(") or (i == "}" and stack[-1] == "{") or (i == "]" and stack[-1] == "[")):
                    stack.pop()
                else: 
                    return False
        return True if len(stack)==0 else False
        