class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        i = 0
        j = 0
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        elif n == 0:
            pass
        else:
            while True:
                if nums1[i] <= nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    nums3.append(nums2[j])
                    j += 1
                if i == m or j == n:
                    break
            if i == m:
                nums3 += nums2[j:]
            else:
                nums3 += nums1[i:]
            
            for i in range(len(nums1)):
                nums1[i] = nums3[i]
        