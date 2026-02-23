#%% 1. Find the kth smallest element element in a given array - QUICKSELECT

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

arr_sort = sorted(arr)
print(arr_sort[k-1])



#%% 2. The arr contains height of towers and we 'have' to adjust there height either add or substract 'k.. AND find the minimum height difference (They are sorted?)
# We need to substract from the highest number and add in lowest number so that the difference can be minute
k_elem = 2
my_arr = [1, 5, 8, 10]

# Greedy Approach

def find_elem(arr, k):
    arr.sort()
    n = len(arr)
    ans = arr[-1] - arr[0] # Fall back plan if the things doesnt go well
    
    for i in range(1, n):
        if arr[i] - k < 0:  #Check negative number
            continue
        
        min_ht = min(arr[0] + k, arr[i] - k)
        max_ht = max(arr[i-1] + k, arr[-1] - k)
        
        ans = min(ans, max_ht - min_ht)
    
    
    return ans

print(find_elem(my_arr, k_elem))

Wrong
len_arr = len(my_arr)
n_arr = []

for i in range(len(my_arr)):
    if i < len_arr//2 - 1:
        n_arr.append(my_arr[i] + k_elem)
    
    else:
        n_arr.append(my_arr[i] - k_elem)
    
print(n_arr)

print(max(n_arr)-min(n_arr))


# #  HW # #


#%% 3. Minimum jumps to get at the end of the array

my_arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
my_other_arr = [0, 10, 20]

def jump_arr(arr):
    n = len(arr)
    i = 0
    count_rotation = 0
    
    while i < n:
        
        if arr[i] == 0:
            return -1
        
        else:
            i += arr[i]
            count_rotation += 1
            
    return count_rotation

print(jump_arr(my_arr))



#%% 4.  Find the duplicate element

my_nums = [1,3,4,2,2]

def find_dup(nums):
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break
        
    slow = nums[0]
        
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    # return slow
    


print(find_dup(my_nums))



#WRONG
def find_dup(nums):
    n = len(nums)
    dot = {}
    
    for i in range(0, n):
        if nums[i] not in dot:
            dot[nums[i]] = i        
        else:
            return nums[i]
    
print(find_dup(my_nums), "is the duplicate element")



#%% 5. Given 2 sorted array we have to merge these elements into one without using any extra space
# The space expand to only those two arrays and we have sort it
# Repeated elements can be inserted
# Took 2 days


arr_a = [2, 4, 7, 10]
arr_b = [2, 3]

def merge_arrays(a, b):
    len_a = len(a)
    # len_b = len(b)
    
    
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] in a:
                if len_a > i:
                    a.insert(i, b.pop(j))
                else:
                    b.insert(j, a[i])
                    a.pop(i)
            elif a[i] > b[j]:
                if len_a > b[j]:    
                    pass
            elif a[i] < b[j]:
                pass
            
    return a, b




#%% 6. 