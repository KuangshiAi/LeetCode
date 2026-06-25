class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left = 0
        right = len(height)-1
        while left < right:
            h = min(height[left], height[right])
            if (right-left)*h > max_water:
                max_water = (right-left)*h
            if height[left+1]>height[left]:
                left+=1
                continue
            elif height[right-1]>height[right]:
                right-=1
                continue
            else:
                break
        return max_water
            