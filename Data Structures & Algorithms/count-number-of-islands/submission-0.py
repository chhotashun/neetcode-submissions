class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            queue = deque()
            grid[row][col] = "0"
            print("Grid position value: ", grid[row][col])
            queue.append((row, col))

            while queue: 
                row, col = queue.popleft()
                print("row is ", row, "column is ", col)
                for row_d, col_d in directions:
                    new_row, new_col = row_d + row, col_d + col 
                    print("New row value: ", new_row, "New col value: ", new_col)
                    if (new_row < 0 or new_col < 0 or 
                    new_row >= rows or new_col >= cols or 
                    grid[new_row][new_col] == "0"):
                        continue 
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    result += 1
        return result 
