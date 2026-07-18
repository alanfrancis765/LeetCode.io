class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return 

            grid[r][c] = "0"

            dfs(r-1, c) #up
            dfs(r+1, c) #down 
            dfs(r, c-1) #left
            dfs(r, c+1) #right   

        island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i, j)
        
        return island 