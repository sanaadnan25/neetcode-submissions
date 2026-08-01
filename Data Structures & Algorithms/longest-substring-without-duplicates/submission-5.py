class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > 0:
            maxim = 1
        else:
            return 0
        right = 1
        left = 0
        seen = set()
        seen.add(s[left])
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right +=1
            else:
                if (right - left) > maxim:
                    maxim = (right - left)
                seen.remove(s[left])
                left += 1
        if (right - left) > maxim:
            maxim = (right - left)       
        return maxim


