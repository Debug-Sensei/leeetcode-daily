class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        drank = numBottles
        empties = numBottles

        while empties >= numExchange:
            empties -= numExchange     # give away empties
            numExchange += 1           # cost increases
            drank += 1                 # one new bottle drunk
            empties += 1               # new empty after drinking

        return drank