class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        answer = 0
        for num in table:
            if num - 1 not in table:
                l = 1
                while num + l in table:
                    l += 1
                answer = max(answer, l)
        return answer