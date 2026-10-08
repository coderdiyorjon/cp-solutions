class Solution(object):
    def removeOuterParentheses(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        counter = 1
        primitiveParenthese = "("
        res: list[str] = []
        for char in s[1:]:
            if char == '(':
                counter += 1
                primitiveParenthese += char
            else:
                counter -= 1
                primitiveParenthese += char

                if not counter: 
                    res.append(primitiveParenthese[1: -1])
                    primitiveParenthese = ""
                    counter = 0
        
        return ''.join(res)
