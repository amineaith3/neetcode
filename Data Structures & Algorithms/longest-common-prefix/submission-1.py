class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = ""
        flag = True
        for c in strs[0]:
            for word in strs[1:]:
                if not word.startswith(ans+c):
                    flag = False
            if flag:
                ans += c
            else:
                break
        return ans