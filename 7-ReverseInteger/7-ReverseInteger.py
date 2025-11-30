# Last updated: 11/30/2025, 3:39:42 PM
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        strx = str(x)
        if x < 0:
            rev = strx.strip("-")
            rev = "-" + rev[::-1]
        else:
            rev = strx[::-1]
        
        xrev = int(rev)

        if xrev > 2**31 -1 or xrev < (-2)**31:
            return 0
        else:
            return xrev