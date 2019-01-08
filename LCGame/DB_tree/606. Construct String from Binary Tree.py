# 606. Construct String from Binary Tree
# https://leetcode.com/problems/construct-string-from-binary-tree/
# Step1: Solved 2019-1-8
# Step2: stack method? more faster?
class Solution:

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # LDR
        if t is None:
            return ""
        if t.left is None and t.right is None:
            return str(t.val) + ""
        if t.right is None:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"




