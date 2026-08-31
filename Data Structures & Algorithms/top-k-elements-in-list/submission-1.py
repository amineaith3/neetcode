class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        data, ans = list(), list()
        for k1, v in freq.items():
            data.append((v, k1))
        data.sort(reverse=True)
        for i in range(k):
            ans.append(data[i][1])
        return ans