from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNum = Counter(nums)
        hashNum_most = hashNum.most_common(k)
        res = []
        for element, count in hashNum_most:
            res.append(element)
        return res