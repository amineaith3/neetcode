class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        l, r = 0, len(height) - 1
        ml, mr = height[0], height[-1]
        ans = 0
        while (l < r):
            if height[l] <= height[r]:
                l += 1
                ml = max(height[l], ml)
                ans += (ml - height[l])
            else:
                r -= 1
                mr = max(mr, height[r])
                ans += (mr - height[r])
        return ans