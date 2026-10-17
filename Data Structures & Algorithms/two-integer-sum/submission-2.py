class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i,num in enumerate(nums):
            look = target-num
            if look in ind:
                return [ind[look], i]
            ind[num] = i
            
