class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        bruh = [0] * (2 * n)
        for i in range(n):
            bruh[i] = bruh[n + i] = nums[i]
        return bruh