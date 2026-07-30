class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefix = [0] * len(nums)
        runProd = 1
        for i, num in enumerate(nums):
            runProd *= num
            prefix[i] = runProd
        
        suffix = [0] * len(nums)
        runProd = 1

        temp = nums
        for i, num in enumerate(reversed(temp)):
            runProd *= num
            suffix[i] = runProd

        for i, num in enumerate(nums):
            if i == 0:
                output[0] = suffix[len(nums) - 2]
            elif i == len(nums) - 1:
                output[i] = prefix[len(nums) - 2]
            else:
                output[i] = prefix[i - 1] * suffix[len(nums) - i - 2]

        return output

        

        
                

            