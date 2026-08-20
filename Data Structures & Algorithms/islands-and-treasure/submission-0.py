class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # go at each position and track basically
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        def addRoom(r,c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r,c) in visit):
                return
            queue.append([r,c])
            visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visit.add((r,c))
        
        # this should calculate distance 
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1
