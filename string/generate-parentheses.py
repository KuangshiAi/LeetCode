class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(s, open_used, close_used):
            if open_used == n and close_used == n:
                res.append(''.join(s))
                return
            if open_used <= n:
                s.append('(')
                backtrack(s, open_used+1, close_used)
                s.pop()
            if open_used > close_used:
                s.append(')')
                backtrack(s, open_used, close_used+1)
                s.pop()
        backtrack([],0,0)
        return res