class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return len(nums)
        slow_pointer=0
        fast_pointer=0
        while fast_pointer<len(nums)-2:
            if nums[fast_pointer]<nums[fast_pointer+2]:
                nums[slow_pointer]=nums[fast_pointer]
                slow_pointer+=1
            fast_pointer+=1
        if len(nums)==3:
            nums[slow_pointer]=nums[fast_pointer]
            slow_pointer+=1
        else:
            nums[slow_pointer]=nums[fast_pointer]
            slow_pointer+=1
            nums[slow_pointer]=nums[fast_pointer+1]
            slow_pointer+=1
        return slow_pointer



        