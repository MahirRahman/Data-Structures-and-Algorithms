class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s = set()
        colorToChange = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        def fill(r, c, src, new):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != src:
                return
            if (r, c) in s:
                return
            else:
                s.add((r,c))
                image[r][c] = new
            fill(r + 1, c, src, new)
            fill(r - 1, c, src, new)
            fill(r, c - 1, src, new)
            fill(r, c + 1, src, new)
        fill(sr, sc, colorToChange, color)
        return image
                
#         h, w = len(image), len(image[0])
        
		
#         def dfs( r, c, src_color, new_color):
            
#             if r < 0 or c < 0 or r >= h or c >= w or image[r][c] == new_color or image[r][c] != src_color:
#                 # Reject for invalid coordination, repeated traversal, or different color
#                 return
            
#             # update color
#             image[r][c] = new_color
            
            
#             # DFS to 4-connected neighbors
#             dfs( r-1, c, src_color, new_color )
#             dfs( r+1, c, src_color, new_color )
#             dfs( r, c-1, src_color, new_color )
#             dfs( r, c+1, src_color, new_color )
            
#         # ---------------------------------------------------------------------------
        
#         dfs(sr, sc, src_color = image[sr][sc], new_color = color)
        
#         return image
        
        
    
        
            