#Majority Element II

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        count = collections.Counter(nums)
        res = []
        for n, t in count.items():
            if t > N / 3:
                res.append(n)
        return res
