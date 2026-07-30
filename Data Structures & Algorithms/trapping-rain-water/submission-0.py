class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        maxim = height[0]
        for i, num in enumerate(height):
            if num >= maxim:
                maxim = num
            prefix.append(maxim)

        maxim = height[len(height) - 1]

        temp = height.copy()
        temp.reverse()
        suffix = []
        for i, num in enumerate(temp):
            if num >= maxim:
                maxim = num
            suffix.append(maxim)
        maxarea = 0
        for i, h in enumerate(height):
            area = min(prefix[i], suffix[len(height) - 1 - i]) - height[i]
            if area < 0:
                area = 0
            maxarea += area

        return maxarea
