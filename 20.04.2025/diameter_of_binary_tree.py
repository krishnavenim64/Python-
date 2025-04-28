Class Solution:

    Def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        Ans=0

        Def dfs(root):

            Nonlocal ans

            If not root: return 0

            R=dfs(root.left)

            L=dfs(root.right)

            Ans=max(ans, l+r)

            Return 1+max(l, r)

        

        Dfs(root)

        Return ans



