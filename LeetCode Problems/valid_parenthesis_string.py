#TLEs
class Solution:
    def checkValidString(self, s: str) -> bool:
        def recurse(s, stack):
            for i in range(len(s)):
                char = s[i]
                if char == '(':
                    stack += 1
                elif char == ')':
                    if stack > 0:
                        stack -= 1
                    else:
                        return False
                else:
                    return recurse('(' + s[i+1:], stack) or recurse(')' + s[i+1:], stack) or recurse(s[i+1:], stack)
            return stack == 0
        
        return recurse(s, 0)



# More subtle approach that doesn't TLE
class Solution:
    def checkValidString(self, s: str) -> bool:
        l, r = 0, 0
        for i in range(len(s)):
            l += 1 if s[i] in '(*' else - 1
            r += 1 if s[~i] in ')*' else -1
            
            if l < 0 or r < 0:
                return False

        return True       
