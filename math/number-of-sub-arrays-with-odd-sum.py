class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        # ans = 0
        # prefix = 0
        # even_count = 1
        # odd_count = 0
        # for num in arr:
        #     prefix += num
        #     if prefix % 2 == 0:
        #         ans += odd_count
        #         even_count += 1
        #     else:
        #         ans += even_count
        #         odd_count += 1
        #     ans %= MOD            
        # return ans
        dp = [[0,0], [0,0]]
        counter = 0
        for i in range(len(arr)):
            if i % 2 == 0:
                idx = 0
            else:
                idx = 1
            if arr[i] % 2 == 0:
                dp[0][idx] = dp[0][1-idx] + 1 # as [arr[i]] also counts
                dp[1][idx] = dp[1][1-idx]
            else:
                dp[0][idx] = dp[1][1-idx]
                dp[1][idx] = dp[0][1-idx] + 1
            counter += dp[1][idx]
            counter %= MOD
        return counter
        