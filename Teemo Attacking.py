#Teemo Attacking

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        total = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            if timeSeries[i] < timeSeries[i - 1] + duration:
                total -= timeSeries[i - 1] + duration - timeSeries[i]
        return total