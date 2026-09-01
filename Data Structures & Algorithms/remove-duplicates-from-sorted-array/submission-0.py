class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[cnt] = nums[i]
                cnt += 1
            i += 1
        return cnt