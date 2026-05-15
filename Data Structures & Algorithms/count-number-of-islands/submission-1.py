class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS approach 
        result = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if (row < 0 or col < 0 or row >= rows 
                or col >= cols or grid[row][col] == "0"):
                return 
            grid[row][col] = "0"
            print("Successfuly set grid value to 0? ", grid[row][column])
            for dr, dc in directions: 
                print("grid value: ", grid[row][col])
                print(row + dr, col + dc)
                #print("sending the new grid row and column: ", grid[row + dr][col + dc])
                dfs(row + dr, col + dc)
        
        for row in range(rows):
            for column in range(cols):
                if (grid[row][column] == "1"):
                    dfs(row, column)
                    result += 1
        return result
