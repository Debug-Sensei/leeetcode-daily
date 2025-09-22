from collections import Counter
class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)
        max_freq = max( freq.values() )
        value_counts = Counter(freq.values())
        count = value_counts[max_freq]
        return max_freq*count