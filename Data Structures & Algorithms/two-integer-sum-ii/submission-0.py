class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use enumerate in python
        # approach- two pointers 
        # but how without o(n^2)
        left, right = 0, len(numbers) - 1
        while (left < right):
            print("left pointer: ", left, "right pointer: ", right)
            res = target - numbers[right]
            print("res: ", res)
            if (numbers[left] > res):
                right -= 1
                print("right pointer: ", right )
            elif (numbers[left] < res):
                left += 1
                print("left pointer: ", left)
            else:
                return[left + 1, right + 1]