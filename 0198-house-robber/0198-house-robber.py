class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp = [0] * (n)
        if n <= 1:
            return nums[0]
        
        #Base Case 
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])#don't rob, rob 

        return dp[n-1]
        