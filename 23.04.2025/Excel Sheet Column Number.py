Class Solution:

    Def titleToNumber(self, columnTitle: str) -> int:

        Ans, pos = 0, 0

        For letter in reversed(columnTitle):

            Digit = ord(letter)-64

            Ans += digit * 26**pos

            Pos += 1

            

        Return ans

