from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = [(num, i) for i, num in enumerate(nums)]
        data.sort(key=lambda x: x[0])
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = data[left][0] + data[right][0]
            if current_sum == target:
                return sorted([data[left][1], data[right][1]])
            elif current_sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1] 