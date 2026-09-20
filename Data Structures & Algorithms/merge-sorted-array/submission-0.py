class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n-1
        pos = n+m-1
        while right >= 0 and left >= 0:
            if nums1[left] > nums2[right]:
                nums1[pos] = nums1[left]
                left -= 1
                pos -= 1
            else:
                nums1[pos] = nums2[right]
                right -= 1
                pos -= 1
        while right >= 0:
            nums1[pos] = nums2[right]
            right -= 1
            pos -= 1

        