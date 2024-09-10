class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        i = 0
        j = len(numbers)-1
        while True:
            if numbers[i] + numbers[j] == target:
                res.append(i+1)
                res.append(j+1)
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
        return res    
        