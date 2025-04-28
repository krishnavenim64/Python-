Class Solution:

    Def buddyStrings(self, s: str, goal: str) -> bool:

        If len(s) != len(goal):

            Return False

        If s == goal :

            Frequency = [0]*26

            For ch in s:

                Frequency[ord(ch)-ord(‘a’)] += 1

                If frequency[ord(ch)-ord(‘a’)] == 2:

                    Return True

            Return False

        First_index = -1

        Second_index = -1

        For i in range(len(s)):

            If s[i] != goal[i]:

                If first_index == -1:

                    First_index = i

                Elif second_index == -1:

                    Second_index = i

                Else:

                    Return False

        If second_index == -1:

            Return False

        Return s[first_index]==goal[second_index] and s[second_index] == goal[first_index]

