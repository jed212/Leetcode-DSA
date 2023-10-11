class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            second = target - num
            if second in dict:
                return [dict[second], i]
            dict[num] = i

nums = [2,7,11,15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result) 