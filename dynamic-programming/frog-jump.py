class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) < 2 or stones[1] != 1:
            return len(stones) == 1

        # dp[i]: the list of jump sizes that can reach position i
        dp = {stone: set() for stone in stones}
        dp[1].add(1)

        for stone in stones:
            for k in dp[stone]:
                for step_size in (k-1, k, k+1):
                    if step_size <= 0:
                        continue
                    next_stone = stone+step_size
                    if next_stone == stones[-1]:
                        return True
                    if next_stone in dp.keys():
                        dp[next_stone].add(step_size)
        return len(dp[stones[-1]]) > 0
        