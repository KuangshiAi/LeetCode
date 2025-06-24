class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_map={}
        major=nums[0]
        for i in range(0,len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i],0)+1
            if freq_map[nums[i]] > freq_map[major]:
                major=nums[i]
        return major
        