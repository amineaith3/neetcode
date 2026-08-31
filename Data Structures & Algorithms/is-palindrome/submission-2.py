class Solution:
    def isPalindrome(self, s: str) -> bool:
        bruh = []
        for c in s:
            if c.isalpha():bruh.append(c.lower())
            elif c.isnumeric():bruh.append(c)
        l, r = 0, len(bruh)-1
        while l<r:
            if bruh[l]!=bruh[r]:
                return False
            l+=1
            r-=1
        return True