class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ar = people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        
        while left <= right:
            weight_sum = people[left] + people[right]
            if weight_sum and weight_sum <= limit:
                left+=1
            right-=1
            boats+=1
        return boats
            