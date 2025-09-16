class Solution:
    def replaceNonCoprimes(self, nums):
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1:
                g = math.gcd(stack[-1], stack[-2])
                if g > 1:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append((a * b) // g)
                else:
                    break
        return stack