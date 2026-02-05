# #1. Rotate the array clockwise (NH)
# arr = [1, 2, 3, 4, 5]

# last_element = arr.pop()
# arr.insert(0, last_element)
# print(arr)


# #2. Find the max subarray in a mixed array (NH-Memory)(DO Algorithm)

# arr = [2, 3, -8, 7, -1, 2, 3]
# cur = arr[0]

# for i in range(1, len(arr)): #started from 1 as cur is essently 0 so we will be adding 2: 0 indexed and wasting time
#     cur = cur + arr[i]
#     cur = max(cur, arr[i])
    
# print(cur)


# #HW

# #3- Find a value's index in a given sorted array (O(logn)-Binary Search)(H)


# def add_target(newlst, target):
    
#     newlst.append(target)
    
#     return newlst.index(target)
    

    
    
# def lst_search(arr, k): #needs sorted array
#     l = 0
#     r = len(arr) - 1
#     while l <= r:
#         mid = (l + r)//2
        
#         if arr[mid] == k:
#             return mid
#         elif arr[mid] < k:
#             l = mid + 1
#         else:
#             r = mid - 1

#     return add_target(arr, k)
    


# lst = [1,3,6]
# target_value = 5

# print(lst_search(lst, target_value))

# # for i in range(len(arr)) # O(n) non binary
# #     if k == arr[i]:
# #         print("Index",i)
    
    
# # 4- Return the indices of the numbers that are adding up to the target value;
# #Exactly one solution- no same element twice, and if i + j then not j + i (F- removed break)

# nums = [2,7,11,15]
# target = 13

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target and i != j:
#             print(i,j)
#         #break - we can remove that just start the 2nd loop from one ahead index



#5- Every value jumps the index; the value is 2 so it  make jump of 2 index which lands on 4
# F

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9, 3, 7, 12, 2]

i = 0
while i < len(arr):
    print(arr[i])
    i += arr[i]
    
# step = arr[0] #For loop doesnt updates range everytime
# for i in range(0, len(arr), step):
    
#     print(arr[i])
#     step = arr[i]


