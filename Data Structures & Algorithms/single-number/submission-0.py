class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}

        for num in nums:
            if num in dict.keys():
                dict[num] = 1
            else:
                dict[num] = 0
        
        for key, val in dict.items():
            if val == 0:
                return key
