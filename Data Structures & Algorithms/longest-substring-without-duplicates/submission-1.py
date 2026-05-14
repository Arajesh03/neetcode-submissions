class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l = 0
        result = 0 

        for r in range(len(s)):
            if s[r] in m:
                l = max(m[s[r]]+1,l)
            m[s[r]] = r
            result = max(result, r-l+1)
        return result