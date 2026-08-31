class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = curr = 0
        pref = defaultdict(int)
        pref[0] = 1
        for num in nums:
            curr += num
            diff = curr - k

            ans += (pref[diff])
            pref[curr] = pref[curr] + 1

        return ans