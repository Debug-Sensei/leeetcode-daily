import heapq
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        res = [-1] * n
        next_rain = defaultdict(list)
        for i, lake in enumerate(rains):
            if lake > 0:
                next_rain[lake].append(i)
        
        heap = []
        full = set()
        
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full:
                    return []
                full.add(lake)
                next_rain[lake].pop(0)
                if next_rain[lake]:
                    heapq.heappush(heap, (next_rain[lake][0], lake))
                res[i] = -1
            else:
                if heap:
                    _, dry_lake = heapq.heappop(heap)
                    full.remove(dry_lake)
                    res[i] = dry_lake
                else:
                    res[i] = 1
        return res