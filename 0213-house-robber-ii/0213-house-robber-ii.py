class Solution(object):
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]
            
        def robH(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            dp = [0]*(n)
            
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1]) #rob, don't rob

            return dp[n-1]
        option1 = robH(nums[:-1])
        option2 = robH(nums[1:])

        return max(option1, option2)
        