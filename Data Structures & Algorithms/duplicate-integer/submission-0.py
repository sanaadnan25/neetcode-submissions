class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for val in nums:
            if val in arr:
                return True
            else:
                arr.append(val)
        return False