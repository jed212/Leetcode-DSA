class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for str in strs:
            count = [0] * 26 
            for b in str:
                count[ord(b) - ord("a")] += 1
            group[tuple(count)].append(str)
        return group.values()