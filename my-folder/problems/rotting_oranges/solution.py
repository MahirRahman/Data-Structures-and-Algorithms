class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rotten = collections.deque([])
        fresh = 0
        level = 0
        # directi
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return fresh
        while rotten:
            level += 1
            # n = len(rotten)
            for _ in range(len(rotten)):
                (r,c) = rotten.popleft()
                for (i,j) in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    if 0<=i<n and 0<=j<m and grid[i][j] == 1:
                        rotten.append((i,j))
                        fresh -= 1
                        grid[i][j] = 2
        if fresh > 0:
            return -1
        else:
            return max(level -1,0)
            