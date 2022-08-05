from heapq import merge
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = list(merge(nums1, nums2))
        if len(x) % 2 == 0:
            a = len(x) / 2
            return (x[a] + x[a - 1]) / 2.0
        else:
            return float(x[len(x) / 2])
        