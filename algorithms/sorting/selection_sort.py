#time complexity of o(n^2)
#in place algorithm o(1) space complexity

class Solution:
    def selection_sort(self, arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    def effic_selection_sort(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


    

    #stable selection sort (when two elements are equal the algorithm do not swap their position)

solution = Solution()
print (solution.selection_sort([64, 25, 12, 22, 11]))
print(solution.effic_selection_sort([64, 25, 12, 22, 11]))