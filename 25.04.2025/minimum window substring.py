Class Solution(object):

    Def minWindow(self, s, t):

        “””

        :type s: str

        :type t: str

        :rtype: str

        “””

        # Verify compare both the frequency array of 

        # both current substring of s and t and makes sure 

        # array of substring of s contains atleast if not more than a particular character in t

        Def verify(s_arr, t_arr):

            For i in range(52):

                If s_arr[i] < t_arr[i]:

                    Return False

            Return True



        # make sure t is longer than s

        Ls, lt = len(s), len(t)

        If lt > ls: return “”



        # Initializing Frequency array for string s and t, sliding window variables

        # and Sol list

        Aas, at = [0] * 52, [0] * 52

        I, j = 0, 0

        Sol = [] # (i, j)



        # Populate frequency array of t

        For _ in t:

            If _.isupper():

                At[ord(_) – ord(‘A’)] += 1 # Indices 0 – 25 for uppercase letters

            Else:

                At[ord(_) – ord(‘a’) + 26] += 1 # Indices 26 – 51 for lowercase letters



        # Loop through String s

        While j < len(s):

            # Verify current substring and if valid append start and end to sol list while incrementing i

            While (verify(aas, at)) and ((j – i + 1) >= lt):

                Sol.append((i, j – 1))

                If s[i].isupper():

                    Aas[ord(s[i]) – ord(‘A’)] -= 1

                Else:

                    Aas[ord(s[i]) – ord(‘a’) + 26] -= 1

                I += 1

            # Update index j and increment j

            If s[j].isupper():

                Aas[ord(s[j]) – ord(‘A’)] += 1

            Else:

                Aas[ord(s[j]) – ord(‘a’) + 26] += 1

            J += 1



        # Process the remaining S after j reached end of string

        While (verify(aas, at)) and ((j – i + 1) >= lt):

            Sol.append((i, j – 1))

            If s[i].isupper():

                Aas[ord(s[i]) – ord(‘A’)] -= 1

            Else:

                Aas[ord(s[i]) – ord(‘a’) + 26] -= 1

            I += 1



        # Initialize variabled to keep track of min length and update the string if new min found

        Min_len = float(“inf”)

        Min_str = “”

        For start, end in sol:

            If (end – start + 1) < min_len:

                # Handle index out of bound exception for string slicing

                If end == len(s) – 1:

                    Min_str = s[start:]

                Else:

                    Min_str = s[start: end + 1]

                Min_len = end – start + 1

        Return min_str

