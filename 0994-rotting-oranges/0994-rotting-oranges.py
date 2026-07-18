class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        q = []
        fresh = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 2:
                    q.append((i, j))
                
                elif grid[i][j] == 1:
                    fresh += 1
        
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)] #up, down, right, left
        minutes = 0

        while q and fresh > 0: 

            n = len(q)
            for _ in range(n):
                x, y = q.pop(0)

                for dx, dy in dir:
                    r = x + dx
                    c = y + dy

                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:

                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c))

            minutes += 1

        return minutes if fresh == 0 else -1
        