Class Solution:

    Def simplifyPath(self, path: str) -> str:

        Stack = []

        Paths = path.split(‘/’)



        For pat in paths:

            If pat == ‘..’:

                If stack:

                    Stack.pop()

            Elif pat and pat != ‘.’:

                Stack.append(pat)

        

        Return ‘/’ + ‘/’.join(stack)

