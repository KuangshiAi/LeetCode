class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        i, j = len(num1)-1, len(num2)-1
        res = []
        while i >=0 or j>=0 or carry >0:
            digit1 = ord(num1[i]) - ord('0') if i>=0 else 0
            digit2 = ord(num2[j]) - ord('0')  if j>=0 else 0
            total = digit1 + digit2 + carry
            res.append(chr(total % 10 + ord('0')))
            carry = total // 10
            i -= 1
            j -= 1
        return "".join(res[::-1])

        