class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sort(nums:List[int]) -> List[int]:
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
            sleft = sort(nums[:mid])
            sright = sort(nums[mid:])
            return merge(sleft, sright)
        nums[::] = sort(nums)
