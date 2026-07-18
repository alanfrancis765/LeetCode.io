class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        inf = float('inf')
        dp = [inf]*(amount+1)
        dp[0] = 0

        for x in range(1, amount+1):
            for coin in coins:
                if x - coin >= 0:

                    dp[x] = min(dp[x], 1 + dp[x - coin])
        
        if dp[amount] == inf:
            return -1 

        return dp[amount]