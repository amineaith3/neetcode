class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left]!=val:left+=1
            else:
                if nums[right]!=val:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                else:
                    right -= 1 
        return left
        """
        idx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx
        """