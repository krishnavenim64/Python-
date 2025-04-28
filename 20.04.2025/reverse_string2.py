Class Solution:

    Def reverseStr(self, s: str, k: int) -> str:

        Tab=[]

        For i in range(len(s)):

            If (i//k)%2==0:

               Tab.insert(i-i%k,s[i])

            Else:

                Tab.append(s[i])

        Res=””

        For t in tab:

            Res+=t

        Return res

        



