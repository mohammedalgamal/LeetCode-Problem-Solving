class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(map(int, list(str(eval(''.join([str(i) for i in digits])) + 1))))
        