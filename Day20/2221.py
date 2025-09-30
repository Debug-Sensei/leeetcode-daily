class Solution(object):
    def triangularSum(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        newNums = []
        for i in range(len(nums)-1):
            newNums.append( (nums[i] + nums[i+1]) %10 )
        
        return self.triangularSum(newNums)