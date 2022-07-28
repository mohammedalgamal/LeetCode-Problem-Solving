class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ''
        for i in range(len(s)):
            if s[i] == ' ' and ans == '':
                continue
            if s[i].isalpha() or s[i] == '.':
                break
            if s[i] == '-':
                ans += '-'
                continue
            if s[i] == '+':
                ans += '+'
                continue
            j = i
            while j < len(s) and s[j] >= '0' and s[j] <= '9':
                ans += s[j]
                j += 1
            break
        try: 
            ans = int(ans)
        except ValueError:
            ans = 0
        if ans < -2 ** 31:
            ans = -2 ** 31
        elif ans > (2 ** 31) - 1:
            ans = (2 ** 31) - 1

        return ans