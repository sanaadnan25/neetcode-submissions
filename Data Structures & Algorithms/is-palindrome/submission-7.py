class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        str1 = []
        for val in s:
            if val.isalnum():
                str1.append(val)
        i = 0
        j = len(str1) - 1
        
        while i <= j:
            if str1[i] != str1[j]:
                return False
            i+=1
            j-=1
        return True
            
