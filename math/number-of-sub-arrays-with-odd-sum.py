class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        hashmap = {0:1}
        prefix = 0
        for num in arr:
            prefix += num
            for key, value in hashmap.items():
                if (prefix - key) % 2 == 1:
                    ans += value
            hashmap[prefix] = hashmap.get(prefix, 0) + 1
        return ans
        