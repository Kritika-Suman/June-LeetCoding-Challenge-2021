class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            if i < 0 or i >= row or j < 0 or j >= col: return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + (helper(i - 1, j) + helper(i + 1, j) + helper(i, j - 1) + helper(i, j + 1))
            return 0

        row = len(grid)
        col = len(grid[0])
        ans = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans = max(ans, helper(i, j))
        return ans
