class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = len(arr)
        if m == 0:
            return []

        largest_right = -1
        for i in range((m - 1), -1, -1):
            current = arr[i]
            arr[i] = largest_right
            largest_right = max(largest_right, current)
        return arr