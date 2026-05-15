class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # another dfs method is similar to neetcode (I was writing this initiialy as well)
        adjList = {i: [] for i in range(n)}
        visited = set()

        for node, path in edges:
            adjList[node].append(path)
            adjList[path].append(node)
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for child in adjList[node]:
                if child == parent:
                    continue 
                if not dfs(child, node):
                    return False 
            return True 
        
        if dfs(0, -1) and n == len(visited):
            return True
        return False