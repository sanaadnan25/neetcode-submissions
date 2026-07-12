class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, val in enumerate(nums):
            comp = target - val
            if comp in indices:
                return [indices[comp], i]
            else:
                indices[val] = i
        