class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        for val in s:
            if val in '[{(':    
                stack.append(val)
            else:
                if not stack:
                    return False
                if stack.pop() != pairs[val]:
                    return False
        return len(stack) == 0
        