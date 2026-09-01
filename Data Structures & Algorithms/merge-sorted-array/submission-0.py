class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m+n):
            nums1[i] = nums2[i - m]
        def mergeSort(arr:List[int])->List[int]:
            def merge(left:List[int], right:List[int])->List[int]:
                ans = []
                l, r = 0, 0
                while l < len(left) and r < len(right):
                    if left[l] < right[r]:
                        ans.append(left[l])
                        l += 1
                    else:
                        ans.append(right[r])
                        r += 1
                ans.extend(left[l:])
                ans.extend(right[r:])
                return ans  
            if len(arr)<=1:return arr
            mid = len(arr)//2
            lefty = mergeSort(arr[:mid])
            righty = mergeSort(arr[mid:])
            return merge(lefty, righty)
        nums1[::] = mergeSort(nums1)
