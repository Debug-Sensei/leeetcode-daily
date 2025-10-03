import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []  # min-heap

        # Step 1: Push all boundary cells into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        trapped_water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: Process heap
        while heap:
            height, x, y = heapq.heappop(heap)

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True

                    # If neighbor is lower, water can be trapped
                    trapped_water += max(0, height - heightMap[nx][ny])

                    # Push the higher of (neighbor height, current height)
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))

        return trapped_water