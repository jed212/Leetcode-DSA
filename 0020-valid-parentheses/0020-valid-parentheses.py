class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match_dict = {'(':')', '{':'}', '[':']'}
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif not stack:
                return False
            elif stack and c == ')' or c == ']' or c == '}':
                last = stack.pop()
                
                if last in match_dict and match_dict[last] == c:
                    continue
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False
                    