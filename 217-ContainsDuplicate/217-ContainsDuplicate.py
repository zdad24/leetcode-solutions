# Last updated: 11/30/2025, 3:39:39 PM
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False