import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  # (time, row, col)
        res = 0

        while heap:
            t, r, c = heapq.heappop(heap)
            res = max(res, t)
            if (r, c) == (n-1, n-1):
                return res
            if visited[r][c]:
                continue
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))