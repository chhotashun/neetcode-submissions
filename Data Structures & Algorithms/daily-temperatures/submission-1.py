class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            print([index, value])
            while stack and value > stack[-1][0]:
                stackValue, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append([value, index])
        return res