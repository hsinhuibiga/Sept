#Gas Station

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0 or len(gas) != len(cost):
            return -1
        sum = cur_sum = 0
        start = 0
        for i in range(len(gas)):
            sum += gas[i] - cost[i]
            cur_sum += gas[i] - cost[i]
            if cur_sum < 0:
                cur_sum = 0
                start = i+1
        if sum < 0:
            return -1
        else:
            return start