#Length of Last Word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        left, right = 0, N - 1
        while right >= 0 and s[right] == " ":
            right -= 1
        left = right
        while left >= 0 and s[left] != " ":
            left -= 1
        return right - left