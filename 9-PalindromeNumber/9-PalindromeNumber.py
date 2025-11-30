# Last updated: 11/30/2025, 3:39:41 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strnum = str(x)
        rev = strnum[::-1]
    
        if strnum == rev:
            return True
        else:
            return False