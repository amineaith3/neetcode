class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bruh = set()
        l = 0
        r = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in bruh:
                bruh.discard(s[l])
                l += 1
            bruh.add(s[r])
            ans = max(ans, r - l + 1)
        return ans