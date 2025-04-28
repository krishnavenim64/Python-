Class Solution(object):

    Def findWords(self, words):

        M = {}

        For c in “qwertyuiop”:

            M[c] = 1

        For c in “asdfghjkl”:

            M[c] = 2

        For c in “zxcvbnm”:

            M[c] = 3

        Ans = []

        For w in words:

            Lw = w.lower()

            R = m[lw[0]]

            If all(m[ch] == r for ch in lw):

                Ans.append(w)

        Return ans

