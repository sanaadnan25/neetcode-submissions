class Solution:

    def sum(self, n: int) -> bool:
        total = 0
        while n > 0:
            curr = n % 10
            total += pow(curr, 2)
            n //= 10
        return total
    def isHappy(self, n: int) -> bool:
        sol= []
        while (n != 1) and n not in sol:
           sol.append(n)
           n = self.sum(n)
        if n == 1:
            return True
        else:
            return False

        