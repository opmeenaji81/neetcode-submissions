class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        answer = []
        largest = 0
        for num in nums:
            if num in count_nums: 
                count_nums[num] += 1 
            else:
                count_nums[num] = 1
        while len(answer) != k:
            largest = 0
            for value in count_nums:
                if value in answer:
                    pass
                
                elif count_nums[value] > largest:
                    largest = count_nums[value]
                    preserve = value
            answer.append(preserve)
        return answer
            

        