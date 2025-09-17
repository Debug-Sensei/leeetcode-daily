class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = { '()' , '{}' , '[]' }

        for ch in s:
            stack.append(ch)
            # keep shrinking if the top two form a valid pair
            while len(stack) >= 2 and (stack[-2] + stack[-1]) in pairs:
                stack.pop()
                stack.pop()

        return not stack