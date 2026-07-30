class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortednums = sorted(nums)
        running = []
        running.append(1)
        run = 1
        for i in range(1, len(sorted(nums))):
            num = sortednums[i]
            if num == sortednums[i - 1]:
                pass
            elif num - sortednums[i - 1] == 1:
                run += 1
                running.append(run)
            else:
                run = 1  
        if len(nums) == 0:
            return 0  
        return max(running)        
