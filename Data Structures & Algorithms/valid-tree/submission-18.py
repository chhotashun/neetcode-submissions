class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(n)}
        visited = set() # will be used for checking connectivity 
        #print(edges)
        print(adjList)
        for nodes, paths in edges:
            #print("The value of nodes are: ", nodes, "The value of paths are: ", paths)
            adjList[nodes].append(paths)
            adjList[paths].append(nodes
            )
        #print("Adjacency List made: ", adjList)
        # Approach- 1) Check connectivity, 2) Cycles 
        def dfs(v, parent):
            # base case- if cycle is there, check if node already in set
            # 2) if empty list after running dfs no cycle 
            # else: main dfs logic- add node to set then iterate through its list members 
            visited.add(v)
            print(visited)
            for child in adjList[v]:
                print("The child node is: ", child, "The mapping of the node v: ", adjList[v])
                if child == parent:
                    continue
                elif child in visited:
                    return False 
                else:
                    # so dfs(v,u) where v is the child and u is the parent
                    print("Sending to dfs child: ", child, "parent: ", v)
                    if not dfs(child, v):
                        return False
            return True 

        if not dfs(0, -1):
            return False
        return len(visited) == n
