class Solution(object):
    def reverse(self, n):
        rev = 0
        sign = -1 if n < 0 else 1
        x = abs(n)

        while x > 0:
            rev = rev * 10 + (x % 10)
            x = x // 10
        rev *= sign

        if rev < -2**31 or rev > 2**31 -1:
            return 0
        return rev 
        
sol = Solution()
result = sol.reverse(-120)
print(result)    
