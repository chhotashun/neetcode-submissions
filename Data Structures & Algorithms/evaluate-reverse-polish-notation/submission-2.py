class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # algorithm- 1) if you see op- add the numbers and store to stack before them
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 - s2)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(int(s1 / s2))
            else:
                stack.append(int(i))
        return int(stack.pop())