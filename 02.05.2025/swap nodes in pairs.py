Class Solution:

    Def swapPairs(self, head):

        If head is None or head.next is None:

            Return head



        Temp = head.next

        Head.next = self.swapPairs(head.next.next)

        Temp.next = head



        Return temp

