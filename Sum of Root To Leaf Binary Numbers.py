#Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = 0
        self.dfs(root, root.val)
        return self.res

    def dfs(self, root, preSum):
        if not root.left and not root.right:
            self.res = (self.res + preSum) % (10 ** 9 + 7)
            return
        if root.left:
            self.dfs(root.left, preSum * 2 + root.left.val)
        if root.right:
            self.dfs(root.right, preSum * 2 + root.right.val)