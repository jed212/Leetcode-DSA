class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] != val:
                left += 1
                k += 1
            else:
                nums[left] = nums[right]
                right -= 1
        return k