class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] +=1
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        elements = []
        for i in range(k):
            val, key = heapq.heappop(heap)
            elements.append(key)
        return elements

        
        