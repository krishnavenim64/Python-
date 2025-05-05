Class Solution(object):

    Def subsetsWithDup(self, nums):

        “””

        :type nums: List[int]

        :rtype: List[List[int]]

        “””

        Numbers=sorted(nums)

        #at every integer in nums we can either add it or not add it to the solution

        #this creates a tree of possibilites, left is add, right is don’t add. 

        #if we write an algorithm to create this tree, storing every leaf node in a set,

        #we can return the set

        Seen=set()

        Possibilities = [[]]  #create the initial none set, which is always a solution

        For i in range(len(numbers)):

            This_num=numbers[i]



            For j in range(len(possibilities)):

                #going through every branch, adding possibility

                New_possibility = possibilities[j][:]

                New_possibility.append(this_num)

                Tupled=tuple(new_possibility)

                If tupled in seen:

                    Continue 

                #we haven’t seen this possibilit before,

                #add a possibility where this element was added on

                #to the possibilities list and the seen hashmap

                Seen.add(tupled)

                Possibilities.append(new_possibility)

        Output_list=[[]]

        For i in range(len(possibilities)):

            If possibilities[i] in output_list:

                Continue

            Else:

                Output_list.append(possibilities[i])

        Return sorted(output_list)

