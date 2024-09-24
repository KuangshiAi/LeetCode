class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hashmap = {}
        for num1 in nums1:
            for num2 in nums2:
                if num1+num2 in hashmap:
                    hashmap[num1+num2] += 1
                else:
                    hashmap[num1+num2] = 1
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in hashmap:
                    count += hashmap[-(num3+num4)]
        return count
        