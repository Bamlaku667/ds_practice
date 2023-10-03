# in a given list find the leader(leaders)
# a number is a leader if it is greater than the elements to the right
# a right most element is always a leader

# naive approach
# o(n^2)
def find_leader(arr, n):
    leader_list = []
    for i in range(n):
        picked = arr[i]
        for j in range(i+1, n):
            if arr[j] >= picked:
                break
            
        if j == n-1:
            leader_list.append(arr[i])

    for leader in leader_list:
        print(leader, end = " ")
    
    print()

#using the suffix maximum algorithm (traversing from left to right)

def find_leader_using_suffix_max(arr, n):
    max_num = arr[n -1 ]
    max_num_stack = [max_num]

    
    for i in range(n-2, 0, -1):
        
        if max_num < arr[i]:
            max_num_stack.append(arr[i])
            max_num = arr[i]

    for num in max_num_stack[::-1]:
        print(num, end= " ")
    print()

def main():
    arr = [16, 17, 4, 3, 5, 2]
    n = len(arr)
    print("using naive approach")
    find_leader(arr, n)
    print('using max suffix algo')

    find_leader_using_suffix_max(arr, n)


if __name__ == "__main__":
    main()





