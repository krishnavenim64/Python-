Class Solution:

    Def pivotIndex(self, arr, l, r):

        While l < r:

            Mid = l + (r – l) // 2

            If arr[mid] > arr[r]:

                L = mid + 1

            Else:

                R = mid

        Return r



    Def binarySearch(self, arr, l, r, target):

        While l <= r:

            Mid = l + (r – l) // 2

            If arr[mid] == target:

                Return mid

            Elif arr[mid] > target:

                R = mid – 1

            Else:

                L = mid + 1

        Return -1



    Def search(self, arr, target):

        N = len(arr)

        Pivot_index = self.pivotIndex(arr, 0, n – 1)

        Idx = self.binarySearch(arr, 0, pivot_index – 1, target)

        If idx != -1:

            Return idx

        Return self.binarySearch(arr, pivot_index, n – 1, target)

