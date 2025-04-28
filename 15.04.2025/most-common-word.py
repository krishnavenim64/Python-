Paragraph=paragraph.lower()

        S=””; di={}

        For i in paragraph:

            If(i not in (“!?’,;. “)):

                S=s+i

            Else:

                If((s not in banned) and s!=””):

                    If(s in di.keys()):

                        Di[s]+=1

                    Else:

                        di.setdefault(s,1)

                s=””

        maxv,maxk=0,s

        for key,value in di.items():

            if(value>maxv):

                maxv=value; maxk=key

        return maxk

