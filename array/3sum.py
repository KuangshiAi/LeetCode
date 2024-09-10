class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        i = 0
        j = i + 1
        k = len(nums) - 1
        res = []
        while True:
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    break
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            
            i += 1
            j = i +1
            k = len(nums) - 1
            if i == len(nums) - 2:
                break
        return res
        