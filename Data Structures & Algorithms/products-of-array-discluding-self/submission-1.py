class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        maxprod = 1
        for num in nums:
            if num!= 0:
                maxprod *= num
            else:
                zeros += 1
        if zeros > 1:
            return [0] * len(nums)
        elif zeros == 1:
            ans = []
            for num in nums:
                if num == 0:
                    ans.append(maxprod)
                else:
                    ans.append(0)
            return ans
        else:
            ans = []
            for num in nums:
                ans.append(maxprod//num)
            return ans
        return []