class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.stack)

    def pop(self) -> None:
        self.stack.pop()
        print(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        res = self.stack[0]
        for i in self.stack:
            if i < res:
                res = i
        return res
