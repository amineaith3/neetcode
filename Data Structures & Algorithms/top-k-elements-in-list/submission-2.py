class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        """
        data, ans = list(), list()
        for k1, v in freq.items():
            data.append((v, k1))
        data.sort(reverse=True)
        for i in range(k):
            ans.append(data[i][1])
        return ans
        """
        data = [list() for _ in range(len(nums))] #a revoir
        for key, value in freq.items():
            data[value-1].append(key)
        ans = []
        for i in range(len(data)-1, -1, -1):
            j = len(data[i])
            if 1<=j<=k:
                ans.extend(data[i])
                k -= j
        return ans