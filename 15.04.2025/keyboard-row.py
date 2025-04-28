Class Solution:

    Def findWords(self, words: List[str]) -> List[str]:

        L1=”qwertyuiop”

        L2=”asdfghjkl”

        L3=”zxcvbnm”

        Res=[]

        For word in words:

            W=word.lower()

            If len(set(l1+w))==len(l1) or len(set(l2+w))==len(l2) or len(set(l3+w))==len(l3) :

                Res.append(word)

        Return res



