class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def valid(k):
            if len(str1) % k or len(str2) % k:
                return False
            n1 = len(str1) // k
            n2 = len(str2) // k
            base = str1[:k]
            return str1 == base * n1 and str2 == base * n2
        for i in range(min(len(str1), len(str2)), 0, -1):
            if valid(i):
                return str1[:i]
        return ''
        