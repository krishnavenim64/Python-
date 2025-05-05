Class Solution(object):

    Def isSymmetric(self, root):

        “””

        :type root: Optional[TreeNode]

        :rtype: bool

        “””



        # Checks for first 3 nodes in tree(used to check whether the tree consists of only one node, or 2 node or 3 node but the values of 2nd and 3rd nodes are different)

        If root.left==None and root.right==None:

            Return True

        If (root.left!=None and root.right==None) or (root.left==None and root.right!=None):

            Return False

        

        If root.left.val!=root.right.val:

            Return False





        # Queue for left tree 

        Left1=[root.left]

        # Queue for right tree

        Right1=[root.right]





        While len(left1)>0 and len(right1)>0:

            # Check for values in queue(left1 and right1)

            If left1[0].val!=right1[0].val:

                Return False



            # Travel in opposite direction and check whether the mirror element exists or not. Checks left node of left tree and right node of right tree.

            If left1[0].left!=None and right1[0].right!=None:

                Left1.append(left1[0].left)

                Right1.append(right1[0].right)

            Elif left1[0].left==None and right1[0].right!=None:

                Return False

            Elif left1[0].left!=None and right1[0].right==None:

                Return False



            # Same as above but checks for right tree node for left tree and left tree node for right tree

            If left1[0].right!=None and right1[0].left!=None:

                Left1.append(left1[0].right)

                Right1.append(right1[0].left)

            Elif left1[0].right==None and right1[0].left!=None:

                Return False

            Elif left1[0].right!=None and right1[0].left==None:

                Return False

            Left1.pop(0)

            Right1.pop(0)

        

        If len(left1)!=0 or len(right1)!=0:

            Return False

        Return True

