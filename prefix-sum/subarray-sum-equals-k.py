class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # using running prefix and hashmap to solve this
        prefix = 0
        hashmap={0:1}
        res = 0
        for num in nums:
            prefix += num
            res += hashmap.get(prefix-k, 0)
            hashmap[prefix] = hashmap.get(prefix,0) + 1
        return res