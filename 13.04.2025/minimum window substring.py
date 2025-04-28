Class Solution:

    Def minWindow(self, s, t):

        #count each character in t

        T = Counter(t)

        

        #setup counter to search t in s

        Count = Counter()

        Length = len(s)

        

        Left = 0

        Ans = [length, ‘’]

        String = ‘’

        

        For index, char in enumerate(s):#use sliding window to find t in s

            

            #keep moving the right pointer

            String += char

            If t[char]:

                Count[char] += 1

            

            While t <= count:#if every character in t is found in the string minimize window

                Ans = min(ans, [(index – left), string[left:]])#update the answer with minimum length string

                

                If t[s[left]]:

                    Count[s[left]] -= 1

                

                Left += 1

        Return ans[1]







