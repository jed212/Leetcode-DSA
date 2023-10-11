class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float(-inf)
        right, left = len(height) - 1, 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_area