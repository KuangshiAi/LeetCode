class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        res = 0
        while True:
            h = min(height[left], height[right])
            if h * (right-left) > res:
                res = h * (right-left)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            if left == right:
                break
        return res
        