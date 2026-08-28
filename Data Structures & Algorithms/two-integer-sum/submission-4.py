class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bruh = {}
        for i, x in enumerate(nums):
            if target - x in bruh:
                return [bruh[target-x], i]
            else:
                bruh[x] = i
        return [0, 1]