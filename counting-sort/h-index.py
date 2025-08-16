class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # left, right = min(min(citations), len(citations)), min(max(citations), len(citations))
        # def check_h_index(h, citations):
        #     counter = 0
        #     for cite in citations:
        #         if cite >= h:
        #             counter += 1
        #     if counter >= h:
        #         return True
        #     else:
        #         return False
        # while left < right:
        #     mid = (left + right + 1) // 2
        #     if check_h_index(mid, citations):
        #         left = mid
        #     else:
        #         right = mid-1
        # return left
        
        bucket = {}
        for cite in citations:
            bucket[cite] = bucket.get(cite, 0) +1
        counter = 0
        for i in range(max(citations), -1, -1):
            counter += bucket.get(i, 0)
            if counter >= i:
                return i