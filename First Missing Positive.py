#First Missing Positive

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums) + 2): # be careful the start and end
            if i not in nums:
                return i