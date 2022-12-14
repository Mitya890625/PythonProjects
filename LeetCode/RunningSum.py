class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
sol = Solution()
print(sol.runningSum([1,2,3,4,5,6,7]))