class Solution:
    def binary_search(self, arr,  low, high ,  key):
        
        if low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == key:
                return mid

            elif arr[mid] > key:
                return self.binary_search( arr ,low, mid - 1, key)
            
            else:
                return self.binary_search(arr, mid + 1, high, key)
            

        return -1
    
solution = Solution()
arr = [2, 5, 8, 12, 16, 23, 28, 56, 72, 91]
output = solution.binary_search(arr, 0, len(arr) -1 , 23)
print(output)

        

        

