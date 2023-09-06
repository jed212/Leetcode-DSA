class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        for c in s[::-1]:
            if c == ' ':
                if i > 0:
                    return i
            else:
                i += 1
        return i
            
                