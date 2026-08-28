class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bruh = [0] * 26
        for x in s:
            bruh[ord(x) - ord('a')] += 1
        for x in t:
            bruh[ord(x) - ord('a')] -= 1
        for x in bruh: 
            if x !=0:return False
        return True