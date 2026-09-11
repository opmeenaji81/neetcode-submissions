class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read = 0
        write = 0
        for num in nums:
            if num!= val:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write