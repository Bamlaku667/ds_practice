# the following method is inefficient when we use append method because:
# we should resize the array and allocate a new memory location whenever we find a new common element

def find_common_using_append(arr1, arr2):
    i= 0
    j = 0
    common  = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j+=1
        else: 
            common.append(arr1[i])
            i += 1
            j += 1
			        
    return common


def find_common_from_three(arr1, arr2, arr3):
    common = find_common_using_append(arr1, arr2)
    common_from_three = find_common_using_append(arr3, common)
	
    for comm in common_from_three:
	    print(comm, end = " ")
		

# arr1 = [1, 5, 10, 20, 40, 80]
# arr2 = [6, 7, 20, 80, 100]
# arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

# find_common_from_three(arr1, arr2, arr3)


#here is the effiecient method 

# no need of resizing the array and allocate new array location 
# we first allocate with a large size of array with each element zero 
# then we will change the common elements with the zeros element of the allocted array 
# using an array k to simulate the pass by reference 

def find_intersection(arr1, arr2, temp, m, n, k):
	#use two pointer to find the common 
    i = 0
    j = 0
    # m = len(arr1), n = len(arr2)
    while i < m and j < n:
         
        if arr1[i] < arr2[j]:
              i += 1
        elif arr1[i] > arr2[j]:
             j += 1
        else: 
             # here i change the k[0] th element with common element
             temp[k[0]] = arr1[i]
             i += 1
             j += 1
             k[0] = k[0] + 1

def main():
     arr1 = [10, 30, 60, 70, 90, 100]
     arr2 = [30, 40, 50, 80, 90, 110]
     arr3 = [10, 30, 80, 90, 120]

     n1 = len(arr1)
     n2 = len(arr2)
     n3 = len(arr3)

     #here allocate large size to store the common from the two 
     temp = [0] * 100000
     #for the 3 arrays
     result = [0] * 100000
     # initialze the single element array
     k = [0]
    
     find_intersection(arr1, arr2, temp, n1, n2, k)
     # find the size of the temp array 
     temp_size = k[0]
     # update the k with the initial 0 value
     k[0] = 0

     find_intersection(temp, arr3, result, temp_size, n3, k)

     for i in range(k[0]):
          print(result[i] , end = " ")
          

     print()


if __name__ == "__main__":
	main()
