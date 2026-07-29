class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen.keys():
                seen[num] += 1
            else:
                seen[num] = 1
        data = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        answer = []
        counter = 1
        for key in data.keys():
            if counter <= k:
                answer.append(key)
                counter +=1
            else:
                break
        return answer

