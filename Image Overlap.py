#Image Overlap

class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        N = len(A)
        LA = [(xi, yi) for xi in range(N) for yi in range(N) if A[xi][yi]]
        LB = [(xi, yi) for xi in range(N) for yi in range(N) if B[xi][yi]]
        d = collections.Counter([(x1 - x2, y1 - y2) for (x1, y1) in LA for (x2, y2) in LB])
        return max(d.values() or [0])