Class Solution:

    Def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        X1, y1, x2, y2 = rec1

        X3, y3, x4, y4 = rec2

        

        Return not (x3 >= x2 or x1 >= x4 or y1 >= y4 or y3 >= y2)
