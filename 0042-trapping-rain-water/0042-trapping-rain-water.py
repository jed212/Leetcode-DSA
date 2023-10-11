class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        right, left = len(height) - 1, 0
        max_l, max_r = height[left], height[right]
        total = 0
        
        while left < right:
            if max_l < max_r:
                left += 1
                max_l = max(height[left], max_l)
                total += max_l - height[left]
            else:
                right-=1
                max_r = max(max_r, height[right])
                total+= max_r - height[right]
        return total