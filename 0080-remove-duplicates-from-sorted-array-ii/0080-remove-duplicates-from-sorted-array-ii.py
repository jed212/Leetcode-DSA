class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 2
        if len(nums) <= 2:
            return len(nums)
        
        for r in range(2, len(nums)):
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l+=1
        return l
        