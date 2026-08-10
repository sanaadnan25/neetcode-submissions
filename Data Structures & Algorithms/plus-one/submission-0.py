import math
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = 0
        for i, val in enumerate(digits):
            dig += val * (10 ** (len(digits) - 1 - i))
        
        dig += 1

        ans = []
        res = str(dig)
        for i in range(len(res)):
            ans.append(int(res[i]))

        return ans
