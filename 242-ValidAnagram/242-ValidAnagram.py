# Last updated: 11/30/2025, 3:39:36 PM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)

        if (s == t):
            return True
        return False

        