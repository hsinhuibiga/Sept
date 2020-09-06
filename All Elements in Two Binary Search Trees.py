#All Elements in Two Binary Search Trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res = []

        def inorder(root):
            if root is None:
                return 0
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root1)
        inorder(root2)
        return sorted(res)
