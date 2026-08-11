class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x1 = len(str1)
        x2 = len(str2)
        if x1 == x2:
            if str1==str2:
                return str1
            else:
                return ""
        bruh = math.gcd(x1, x2)
        def co(ss, x, word):
            return ss * x == word
        if co(str1[:bruh], x1 // bruh, str1) and co(str2[:bruh], x2//bruh, str2):
            return str1[:bruh]
        else:
            return ""