class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            x = num
            if x-1 in nums:continue
            while x in nums:
                x += 1
                ans = max(ans, x-num)
        return ans
