class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        dicti = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }
        
        for c in s:
            if c in dicti:
                ans.append(c)
            else:
                if not ans or dicti[ans[-1]] != c:
                    return False
                ans.pop()
        
        return len(ans) == 0