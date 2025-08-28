class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k <= 0:
            return []

        n1, n2 = len(nums1), len(nums2)

        # Min-heap initialization
        # Push up to k pairs (nums1[i] + nums2[0], i, 0)
        heap= []
        limit = min(k, n1)
        for i in range(limit):
            # push tuple of (sum, i, j)
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        res=[]

        # Extract the smallest sum pairs up to k times
        while heap and len(res) < k:
            s, i, j = heapq.heappop(heap)  # pop smallest sum
            res.append([nums1[i], nums2[j]])  # record the actual pair
            if j + 1 < n2:
                # push the next pair for same i with next j
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
