class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match_dict = {')':'(', '}':'{', ']':'['}
        
        for c in s:
            if c not in match_dict:
                stack.append(c)
                continue
            if not stack or match_dict[c] != stack[-1]:
                return False
            stack.pop()
            
        return not stack