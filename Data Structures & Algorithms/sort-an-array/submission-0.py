class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left:List[int], right:List[int]) -> List[int]:
            ans = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    ans.append(left[i])
                    i += 1
                else:
                    ans.append(right[j])
                    j += 1
            ans.extend(left[i:])
            ans.extend(right[j:])
            return ans

        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        lefty = nums[:mid]
        righty = nums[mid:]
        sleft = self.sortArray(lefty)
        sright = self.sortArray(righty)
        return merge(sleft, sright)
        