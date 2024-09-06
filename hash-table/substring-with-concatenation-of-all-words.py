class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s)
        m = len(words[0])
        k = len(words)
        p = m * k
        res = []
        valid = set()

        def validsubstring(str, words, m):
            i = 0
            temp_words = words[:]
            while i < p:
                cur_word = str[i:i+m]
                if cur_word in temp_words:
                    temp_words.remove(cur_word)
                i += 1
            return temp_words == []
        
        j = p
        while j <= len(s):
            if s[j-p:j] in valid:
                res.append(j-p)
            elif validsubstring(s[j-p:j], words, m):
                res.append(j-p)
                valid.add(s[j-p:j])
            j += 1
        
        return res
        