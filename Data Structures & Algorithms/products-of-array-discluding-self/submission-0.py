class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [0] * len(nums)
        multiply = 1
        for i in range(len(nums)):
            multiply = nums[i] * multiply
            prefix.append(multiply)
        multiply = 1
        for j in range(len(nums) - 1, -1, -1):
            multiply = multiply * nums[j]
            postfix[j] = multiply
        output = []
        for x in range(len(nums)):
            y = x - 1
            z = x + 1
            if (y < 0):
                output.append(postfix[z])
            elif (z > len(postfix) - 1):
                output.append(prefix[y])
            else:
                result = prefix[y] * postfix[z]
                output.append(result)
        return output
