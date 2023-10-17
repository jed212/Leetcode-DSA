class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = max(piles)
        left, right = 1, max(piles)
        
        while left <= right:
            k = (right + left)// 2
            time_taken = 0
            
            for pile in piles:
                time_taken += math.ceil(pile/k)
            if time_taken <= h:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1

        return result