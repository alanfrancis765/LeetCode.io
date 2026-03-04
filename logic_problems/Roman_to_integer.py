class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        prev = 0
        total = 0
        for i in reversed(s):
            value = roman[i]
            if prev > value : total -= value
            else : total += value 
            prev = value 
        return total 
sol = Solution()
result = sol.romanToInt("MCMXCIV")
