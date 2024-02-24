class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in ("+", "-", "*", "/"):
                value = eval(stack[-2] + tokens[i] + stack.pop())
                stack.pop()
                value = math.floor(value) if abs(value)==value else math.ceil(value)
                stack.append(str(value))
            else:
                stack.append(tokens[i])

        return int(stack[0])
        