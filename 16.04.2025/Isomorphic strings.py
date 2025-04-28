Class Solution:

    Def isIsomorphic(self, s: str, t: str) -> bool:

        My_dict = {}

        For i,j in zip(s,t):

            If my_dict.get(i) == None and j not in my_dict.values():

                My_dict[i] = j

            If my_dict.get(i) == None and j in my_dict.values():

                Return False

            Elif my_dict.get(i) != None and my_dict.get(i) != j:

                Return False

        Return True

