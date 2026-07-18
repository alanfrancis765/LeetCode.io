class Solution:
    def strStr(self, haystack, needle):

        n = len(haystack)
        m = len(needle)

        for i in range(n):
            if haystack[i: i+m] == needle:
                return i
        return -1
haystack = "leetcode"
needle = "leeto"
sol = Solution()
result = sol.strStr(haystack, needle)
print(result)