class Solution:

    def encode(self, strs: List[str]) -> str:
        data = []
        for s in strs:
            data.append(str(len(s)) + "?" + s)
        ans = "".join(data)
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        idx = 0
        n = len(s)
        ans = []
        while idx < n:
            j = idx
            while s[j] != "?":
                j += 1
            lenWord = int(s[idx:j])
            word = s[j + 1: j+lenWord + 1]
            ans.append(word)
            idx = j + lenWord + 1
        return ans