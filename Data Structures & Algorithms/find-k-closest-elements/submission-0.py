class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        store = []
        otpt = []
        for i in range(0,len(arr)):
            distance = abs(arr[i] - x)
            store.append((distance, arr[i]))
        store = sorted(store)
        for _ in range(k):
            otpt.append(store[_][1])
        return sorted(otpt)
            
            