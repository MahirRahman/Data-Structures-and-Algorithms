class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        s = set()
        final_count = 0
        def helper(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return  
            if (r,c) in s:
                return
            ur = r - 1
            dr = r + 1
            lc = c - 1
            rc = c + 1
            
            s.add((r,c))
            helper(ur,c)
            helper(dr,c)
            helper(r,lc)
            helper(r,rc)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in s and grid[i][j] == '1':
                    helper(i,j)
                    final_count += 1
        return final_count