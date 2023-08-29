class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans, cpy = [], nums.copy()
        for i in range(len(nums)):
            ans.append(nums[i])
        ans.extend(cpy)
        return ans