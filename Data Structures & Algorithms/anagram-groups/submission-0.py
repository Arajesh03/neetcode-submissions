from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            sorted_tuple = tuple(sorted(s))
            hashMap[sorted_tuple].append(s)

        return list(hashMap.values())