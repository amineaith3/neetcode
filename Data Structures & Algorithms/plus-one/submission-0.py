class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(x) for x in digits]
        return list(str(int("".join(digits)) + 1))