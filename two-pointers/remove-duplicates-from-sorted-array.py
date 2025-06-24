class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow_pointer=1
        fast_pointer=0
        while fast_pointer<len(nums)-1:
            if nums[fast_pointer] < nums[fast_pointer+1]:
                nums[slow_pointer] = nums[fast_pointer+1]
                slow_pointer += 1
            fast_pointer += 1
        return slow_pointer
        