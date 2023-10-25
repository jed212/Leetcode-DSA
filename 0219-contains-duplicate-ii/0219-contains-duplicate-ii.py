class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
                if num in hashmap and (abs(i-hashmap[num])<= k):
                    return True 
                hashmap[num] = i

# nums =  [1,2,3,1]
# k = 3
# solution = Solution()
# result = solution.containsNearbyDuplicate(nums, k)
