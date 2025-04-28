Letters = “abcdefghijklmnopqrstuvwxyz”

        

        

        Morse_code = [“.-“, “-...”, “-.-.”, “-..”, “.”, “..-.”, “--.”, “....”, “..”, “.---“, “-.-“, “.-..”, “—“, “-.”, “---“, “.--.”, “--.-“, “.-.”, “...”, “-“, “..-“, “...-“, “.—“, “-..-“, “-.—“, “--..”]



      

        Morse_dict = dict(zip(letters, morse_code))



        

        Words2 = []



        For word in words:

      

            K = “”

         

            For i in word:

              

                K += morse_dict[i]



            

            Words2.append(k) 



        Return len(set(words2))

