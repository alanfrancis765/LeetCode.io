class Solution(object):
    def isPalindrome(self, x):
        num = x
        rev = 0

        while num > 0:
            rev = rev * 10 + (num % 10)
            num = num // 10

        return rev == x
sol = Solution()
x = 121

if sol.isPalindrome(x):
    print("Palindrome")
else:
    print("Not Palindrome")
