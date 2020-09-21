#Sequential Digits

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        queue = range(1,10)
        while len(queue) > 0:
            val = queue.pop(0)
            if val >= low and val <= high:
                res.append(val)
            elif val > high:
                continue
            last = int(str(val)[-1])
            if last == 9:continue
            new_val = str(val) + str(last + 1)
            queue.append(int(new_val))
        return sorted(res)