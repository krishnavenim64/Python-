Class Solution(object):

    Def validMountainArray(self, arr):

        “””

        :type arr: List[int]

        :rtype: bool

        “””

        Mountain_found = False

        Size = len(arr)

        

        # Ceases to be a mountain when:

        # - Two neighboring elements are the same

        # - Comparison fails after peak is found

        # - Size of array is < 3 (edge case)

        # - First two elements fail uphill comparison (left_val < right_val) (edge case)



        If size < 3 or (arr[0]>arr[1]):

            Return False



        For i in range(1, size):

            If arr[i-1] > arr[i] and not mountain_found:

                # We found the peak

                Mountain_found = True

            Elif (arr[i] == arr[i-1]) or ((arr[i-1] < arr[i]) and mountain_found):

                # Downhill comparison (left_val > right_val) failed after the peak is found

                Mountain_found = False

                # Once it ceases to be a mountain, stop iteration

                Break    

        Return mountain_found

        

