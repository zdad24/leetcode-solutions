# Last updated: 11/30/2025, 3:39:38 PM
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running = []
        total = 0
    
        for num in nums:
            total+= num
            running.append(total)
            
        return running

        return running
        