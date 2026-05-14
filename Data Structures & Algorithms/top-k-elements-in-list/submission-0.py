from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNum = Counter(nums)
        hashNum_most = hashNum.most_common(k)
        result=[]
        for element, count in hashNum_most:
            result.append(element)

        return result