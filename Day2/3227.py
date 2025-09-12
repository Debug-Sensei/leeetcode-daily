class Solution(object):
    def doesAliceWin(self, s):
        # Count how many vowels are in the string
        # Alice wins if there's at least one vowel, because:
        # - She can always remove a substring with exactly 1 vowel (odd count).
        # - That guarantees she gets the first valid move.
        # - If no vowels exist, Alice cannot move and loses immediately.
        return sum(1 for ch in s if ch in "aeiou") > 0
