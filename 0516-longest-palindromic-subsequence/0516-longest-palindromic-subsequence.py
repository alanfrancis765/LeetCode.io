class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s1 = s
        s2 = s1[::-1]
        n = len(s)

        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):

                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[n][n]