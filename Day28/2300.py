import bisect

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        ans = []
        for s in spells:
            need = (success + s - 1) // s  # ceil(success / s)
            idx = bisect.bisect_left(potions, need)
            ans.append(m - idx)
        return ans