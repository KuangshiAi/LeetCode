class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        prefix = 0
        even_count = 1
        odd_count = 0
        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                ans += odd_count
                even_count += 1
            else:
                ans += even_count
                odd_count += 1
            ans %= MOD            
        return ans
        