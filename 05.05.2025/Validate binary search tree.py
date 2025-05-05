Class Solution(object):

    Def isValidBST(self, root):

        “””

        :type root: Optional[TreeNode]

        :rtype: bool

        “””

        Def isValid(root, max, min):

            If root is None:

                Return True



            If min < root.val < max:

                Return isValid(root.left, root.val, min) and isValid(root.right, max, root.val)



            Return False



        Return isValid(root, float(“inf”), float(“-inf”))

