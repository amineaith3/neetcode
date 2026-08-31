class Solution:
    def validPalindrome(self, s: str) -> bool:
        bruh = [0] * 26
        for c in s:
            bruh[ord(c) - ord('a')] += 1
        where = []
        for i, b in enumerate(bruh):
            if b%2:
                where.append(i)
        if len(where) > 2:
            return False 
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                #left is issue:
                newL1, newR1 = l + 1, r
                lefty = True
                while newL1 < newR1:
                    if s[newL1] != s[newR1]:
                        lefty=False
                        break
                    newL1 += 1
                    newR1 -= 1
                newL2, newR2 = l, r - 1
                righty = True
                while newL2 < newR2:
                    if s[newL2] != s[newR2]:
                        righty=False
                        break
                    newL2 += 1
                    newR2 -= 1
                return lefty or righty
        return True