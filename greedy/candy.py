class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        left = []
        right = []
        for i in range(len(ratings)):
            left.append(1)
            right.append(1)
        for i in range(len(ratings)):
            if i > 0 and ratings[i-1] < ratings[i]:
                left[i] = left[i-1] + 1
        for j in range(len(ratings)-1, -1, -1):
            if j < len(ratings)-1 and ratings[j] > ratings[j+1]:
                right[j] = right[j+1] + 1
        res = 0
        for i in range(len(ratings)):
            res += max(left[i], right[i])
        return res

        