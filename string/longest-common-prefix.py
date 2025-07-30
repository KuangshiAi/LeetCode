class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if len(strs) == 0:
        #     return ""
        # res = strs[0]
        # for i in range(1, len(strs)):
        #     while strs[i].find(res) != 0:
        #         res = res[:len(res)-1]
        #         if res == "":
        #             return ""
        # return res
        
        # divide and conquer
        def LCP(left, right):
            min_len = min(len(left), len(right))
            res = ""
            for i in range(min_len):
                if left[i] == right[i]:
                    res += left[i]
                else:
                    break
            return res
        
        def divide_and_conquer(strs, l, r):
            if l == r:
                return strs[l]
            else:
                mid = (l+r) // 2
                left_lcp = divide_and_conquer(strs, l, mid)
                right_lcp = divide_and_conquer(strs, mid+1, r)
                return LCP(left_lcp, right_lcp)
        
        return divide_and_conquer(strs, 0, len(strs)-1)