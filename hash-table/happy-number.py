class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_set = set()
        sum = 0
        while True:
            sum = 0
            while n:
                n, r = divmod(n, 10)
                sum = sum + r**2
            if sum == 1:
                return True
            elif sum in sum_set:
                return False
            else:
                sum_set.add(sum)
                n = sum