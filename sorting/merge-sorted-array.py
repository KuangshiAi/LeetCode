class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        if m == 0:
            for q in range(n):
                nums1[q] = nums2[q]
        elif n == 0:
            pass
        else:
            while True:
                if nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                    k -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                    k -= 1
                if j < 0 or i < 0:
                    break
            if i < 0:
                nums1[:j+1] = nums2[:j+1]
        