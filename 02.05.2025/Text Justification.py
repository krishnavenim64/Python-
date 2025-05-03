Class Solution(object):

    Def fullJustify(self, words, maxWidth):

        “””

        :type words: List[str]

        :type maxWidth: int

        :rtype: List[str]

        “””

        Line_start = 0

        Groups = []

        While line_start < len(words):

            Line_char_count = 0

            I = line_start

            While i < len(words) and line_char_count + ((i-line_start)-1) + len(words[i]) < maxWidth:

                Line_char_count += len(words[i])

                I += 1

            Groups.append((line_start, i, line_char_count))

            Line_start = i



        Lines = []

        For (start, end, nchars) in groups[0:-1]:

            Padding = maxWidth – nchars

            If end-start == 1:

                Lines.append(words[start] + “ “ * padding)

                Continue

            Q, r = divmod(padding, end-start-1)

            Line = []

            For i in range(0, end-start):

                Spaces = (q + (i < r))

                If i == end-start-1:

                    Line.append(words[end-1])

                Else:

                    Line.append(words[start+i] + “ “ * spaces)

            Lines.append(“”.join(line))

        

        Last_line = groups[-1]

        Last = “ “.join(words[last_line[0]:last_line[1]])

        Last = last + “ “ * (maxWidth – len(last))

        Lines.append(last)

        Return lines

