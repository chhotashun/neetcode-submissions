class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # O(n^2) brute force 
        left = 0
        n = len(arr)
        while (left < n - 1):
            right = left + 1
            max_num = arr[right]
            while (right < n):
                if arr[right] > max_num:
                    max_num = arr[right]
                right += 1
            arr[left] = max_num
            print(arr)
            left += 1
        arr[n - 1] = -1
        return arr
