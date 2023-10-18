class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if not nums:
            return 0
        
        while left <= right:
            mid = (right + left) //2
            
            if nums[right] > nums[left]:
                return nums[left]
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -=1
        return nums[left]