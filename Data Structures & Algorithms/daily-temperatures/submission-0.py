class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # gonna store as [value, index]

        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                # do logic 
                stackValue, stackIndex = stack.pop()
                res[stackIndex] = (index - stackIndex)
            stack.append([value, index])
            print("stack structure: ", stack)
        return res