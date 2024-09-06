class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = 0
        cur_sum = 0
        i = 0
        j = 0
        while j < len(nums):
            cur_sum += nums[j]
            j += 1

            if cur_sum >= target:
                while cur_sum > target:
                    cur_sum = cur_sum - nums[i]
                    i += 1
                if cur_sum == target:
                    cur_len = j - i
                else:
                    cur_len = j - i +1
                if min_len == 0:
                    min_len = cur_len
                else:
                    min_len = min(min_len, cur_len)

        return min_len
                
        