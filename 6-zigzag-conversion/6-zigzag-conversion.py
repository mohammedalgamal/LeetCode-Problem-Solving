class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = [[] for x in range(n)]
        idx = list(range(n)) + list(range(n - 2, 0, -1))
        st = ''

        for i in range(len(s)):
            ans[idx[i % len(idx)]].append(s[i])    

        for i in range(n):
            st += ''.join(ans[i])
        
        return st