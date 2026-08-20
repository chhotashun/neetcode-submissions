class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh = 0
        time = 0

        # got all rotten fruits 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        print(fresh)

        # bfs should basically add the neighbours of rotten to the queue 
        def bfs(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or grid[r][c] == 2 ):
                return False
            q.append([r,c])
            grid[r][c] = 2
            #fresh -= 1
            return True

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                # run bfs to add its neighbours and after adding neighbours turn grid[r][c] == 2 and increment time 
                if bfs(row + 1,col): fresh -= 1
                if bfs(row - 1, col): fresh -= 1
                if bfs(row, col + 1): fresh -= 1
                if bfs(row, col - 1): fresh -= 1
            time += 1
                # bfs should return queue with neihgbours 
        return time if fresh == 0 else -1
