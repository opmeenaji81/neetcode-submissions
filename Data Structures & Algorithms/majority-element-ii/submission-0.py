class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        new = []
        for num in nums:

            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            if count[num] > len(nums) //3 and num not in new:
                new.append(num)
        return new