class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not image:
            return 

        rows = len(image)
        cols = len(image[0])

        oldcolor = image[sr][sc] #1

        if oldcolor == color:
            return image

        def dfs(r, c):

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or 
                image[r][c] != oldcolor):
                return 

            image[r][c] = color 
            dfs(r-1, c) #up
            dfs(r+1, c) #down
            dfs(r, c-1) #left
            dfs(r, c+1) #right

        dfs(sr, sc)
        
        return image
            

