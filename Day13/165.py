class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        # Pad shorter list with zeros
        n = max(len(v1), len(v2))
        v1.extend([0] * (n - len(v1)))
        v2.extend([0] * (n - len(v2)))
        
        # Compare element by element
        for a, b in zip(v1, v2):
            if a < b:
                return -1
            elif a > b:
                return 1
        return 0