class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for word in strs:
            char_set = tuple(sorted(list(word)))
            if char_set not in res.keys():
                res[char_set] = [word]
            else:
                res[char_set].append(word)
            
        return res.values()      