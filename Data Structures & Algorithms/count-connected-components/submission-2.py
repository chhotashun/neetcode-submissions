class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # undirected graph so edges go both ways 
        # approach- 1) just iterate through the edges and check if they are in visited 
        # if not increase counter 
        result = 0
        visited = set()
        adjList = {i : [] for i in range(n)}
        print(adjList)

        for node, edge in edges:
            adjList[node].append(edge)
            adjList[edge].append(node)
        print(adjList)

        # dfs loop should be to iterate over edges of nodes 
        # to check for connected components what I need to do is check if visited == n
        # if not iterate over the other nodes 
        def dfs(node, parent):
            print("Node going: ", node)
            visited.add(node)
            for child in adjList[node]:
                if child == parent or child in visited:
                    continue 
                dfs(child, node)
                print("The child of node: ", child)

        for i in range(n):
            if i not in visited:
                print("dfs child running on: ", i)
                dfs(i, -1)
                result += 1
        return result