class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in nums:
            x = num
            if x-1 in s:continue
            while x in s:
                x += 1
                ans = max(ans, x-num)
        return ans
