Class MyQueue:



    Def __init__(self):

        Self.s1 = []

        Self.s2 = []



    Def push(self, x: int) -> None:

        Self.s1.append(x)



    Def pop(self) -> int:

        If not self.s2:

            While self.s1:

                # removing the value at the top of the stack

                Self.s2.append(self.s1.pop())

        # return that value

        Return self.s2.pop()



    Def peek(self) -> int:

        If not self.s2:

            While self.s1:

                # removing the value at the top of the stack

                Self.s2.append(self.s1.pop())

        # return the value at the top of s2

        Return self.s2[-1]



    Def empty(self) -> bool:

        Return len(self.s1) == 0 and len(self.s2) == 0



