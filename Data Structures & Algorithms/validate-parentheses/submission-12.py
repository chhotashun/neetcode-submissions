class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        hashmap = {"]" : "[",
                   ")" : "(",
                   "}" : "{"}
        stack = []
        for item in s:
            if item in hashmap:
                if not stack:
                    return False
                tmp = stack.pop()
                if hashmap[item] != tmp:
                    return False
            else:
                stack.append(item)
        return len(stack) == 0