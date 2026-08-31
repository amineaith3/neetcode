class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ss = set(nums)
        ans = 1
        while ans in ss:
            ans += 1 
        return ans