Class Solution:

    Def toGoatLatin(self, sentence: str) -> str:

        Words = sentence.split()

        Vowels = ‘aeiouAEIOU’

        Goat_latin_words = []



        For index, word in enumerate(words):

            If word[0] in vowels:

                Goat_word = word + “ma”

            Else:

                Goat_word = word[1:] + word[0] + “ma”

            

            # Add ‘a’ based on the word index (1-indexed)

            Goat_word += ‘a’ * (index + 1)

            Goat_latin_words.append(goat_word)



        Return ‘ ‘.join(goat_latin_words)



