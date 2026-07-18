class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if expression.isdigit(): #Base Case 
            return [int(expression)]
        result = []
        
        for i, ch in enumerate(expression):
            if ch in "-+*":

                left = self.diffWaysToCompute(expression[:i]) # recursive case 
                right = self.diffWaysToCompute(expression[i+1:]) 

                for l in left:
                    for r in right:

                        if ch == "-":
                            result.append(l-r)
                        elif ch == "+":
                            result.append(l+r)
                        elif ch == "*":
                            result.append(l*r)
                        
        return result
