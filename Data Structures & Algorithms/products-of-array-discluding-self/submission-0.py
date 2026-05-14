class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            print("prefix")
            pref[i] = nums[i - 1] * pref[i - 1]
            print(pref[i])
        for i in range(n - 2, -1, -1):
            print("suff")
            print(nums[i+1])
            print(suff[i + 1])
            suff[i] = nums[i + 1] * suff[i + 1]

            print("----")
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res