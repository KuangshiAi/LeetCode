class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def cal_sum(peak):
            left_sum = 0
            if peak > index:
                left_sum = (peak + peak - index) * (index + 1) // 2
            else:
                left_sum = (peak + 1) * peak // 2 + index - peak + 1
            right_sum = 0
            right_index = n - index - 1
            if peak > right_index:
                right_sum = (peak + peak - right_index) * (right_index + 1) // 2
            else:
                right_sum = (peak + 1) * peak // 2 + right_index - peak + 1
            return left_sum + right_sum - peak

        low, high = 1, maxSum
        while low < high:
            mid = (low + high +1) // 2
            if cal_sum(mid) > maxSum:
                high = mid - 1
            else:
                low = mid
        return low