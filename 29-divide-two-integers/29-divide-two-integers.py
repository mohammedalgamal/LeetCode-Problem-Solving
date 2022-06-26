class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        s = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                count += i
                temp <<= 1
                i <<= 1

        if s:
            count = -count        

        if count <= -2 ** 31:
            return -2 ** 31
        elif count >= 2 ** 31 - 1:
            return 2 ** 31 -1        
        

            
        return count