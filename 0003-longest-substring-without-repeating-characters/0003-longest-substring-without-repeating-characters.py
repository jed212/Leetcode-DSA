class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track_set = set()
        l = 0
        max_length = 0
        
        for r in range(len(s)):
            while s[r] in track_set:
                track_set.remove(s[l])
                l += 1
            max_length = max(max_length, r - l + 1)
            track_set.add(s[r])
        return max_length
        