class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda p: p[1])
        arrow_x = points[0][1]
        res = 1
        for point in points:
            if point[0] > arrow_x:
                res += 1
                arrow_x = point[1]
        return res