Class Solution(object):

    Def simplifyPath(self, path):

        “””

        :type path: str

        :rtype: str

        “””

        Stack=[]

        Path=path.split(“/”)

        Path=[i for i in path if i and i!=”/” and i!=”.”]

        For i in path:

            If i==”..” and stack:

                Stack.pop()

            Elif i!=”..”:

                Stack.append(i)

        Return “/”+”/”.join(stack)

