class Solution(object):
    def isValid(self, s):
        stack = []
        match = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != match[ch]:
                    return False
        return not stack 
sol = Solution()
strs = "(]"
result = sol.isValid(strs)
print(result)        
