class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_small = len(nums) - k
        # use median of medians to solve this problem
        def median_of_medians(nums, k):
            if len(nums) <= 5:
                return sorted(nums)[k]
            medians = []
            for i in range(0, len(nums), 5):
                group = sorted(nums[i:i+5])
                medians.append(group[len(group)//2])
            pivot = median_of_medians(medians, len(medians)//2)
            lows = [x for x in nums if x < pivot]
            pivots = [x for x in nums if x == pivot]
            highs = [x for x in nums if x > pivot]
            if k < len(lows):
                return median_of_medians(lows, k)
            elif k<len(lows)+len(pivots):
                return pivot
            else:
                return median_of_medians(highs, k-len(lows)-len(pivots))
        
        return median_of_medians(nums,k_small)
        