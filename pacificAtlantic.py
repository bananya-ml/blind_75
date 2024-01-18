'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''


class Solution(object):
    def pacificAtlantic(self, heights):
        '''
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        '''
        rows, cols = len(heights), len(heights[0])
        p, a = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, p, heights[0][c])
            dfs(rows-1, c, a, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, p, heights[r][0])
            dfs(r, cols-1, a, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in p and (r, c) in a:
                    res.append([r, c])
        return res
