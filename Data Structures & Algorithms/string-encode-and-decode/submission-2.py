class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        len(s1)s1 len(s2)s2
        """
        ans = ""
        for s in strs:
            nn = len(s)
            if nn < 10:
                ans += "00"
            elif nn < 100:
                ans += "0"
            ans += str(nn)
            ans += s
        print(ans)
        return ans
    def decode(self, s: str) -> List[str]:
        idx = 0
        ans = []
        while idx < len(s):
            l = int(s[idx:idx+3])
            ans.append(s[idx+3:idx+l+3])
            idx += l + 3
        return ans
