from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashNum = Counter(nums)

        for i in hashNum:
            if hashNum[i] > 1:
                return True
        
        return False