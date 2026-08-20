class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use bfs alternatively can use dfs also 
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        islands = 0
        # only do bfs when 1 is spotted 
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if ((new_row) in range(rows) and (new_col) in range(cols) and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited):
                        q.append((new_row,new_col))
                        visited.add((new_row,new_col))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    print("run this: ", True)
                    bfs(r,c)
                    islands += 1
        return islands
            