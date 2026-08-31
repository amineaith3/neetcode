class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n = len(nums)
        for num in nums:
            freq[num] += 1
            if freq[num] > (n//2):
                return num
        return -1