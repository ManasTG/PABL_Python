
#1. Reverse the array; In place- cannot do what is done here(F)
# #arr = [1, 2, 3, 4, 5, 6, 7]

# rev_arr = arr[::-1]
# #OR
# #print(reversed(arr))



# print(rev_arr)


# #2. Find Min and max in a array(NH)

# arr = [2, 3, 1, 4, 8, 6, 7]
# a = arr[0]
# b = arr[0]
# for i in range(len(arr)):
#     if a > arr[i]:
#         a = arr[i]
#     else:
#         pass
    
#     if b < arr[i]:
#         b = arr[i]
#     else:
#         pass
# print(a,b)
    
# # print(min(arr))


# #HW

# #3. Find the smallest array on the index given as 'k'; sort the array before (F)

# arr = [3, 1, 4, 7, 9]
# k = 3

# arr_sort = sorted(arr)

# print(arr_sort[k-1])
        

# #4.Union of two arrays; must be sorted(question says) (NH)

# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7]  #using sorted array    
# c = []
# i = j = 0

# while i < len(a) and j < len(b): 
#     if a[i] < b[j]:
#         c.append(a[i])
#         i += 1
        
#     elif a[i] > b[j]:
#         c.append(b[j])
#         j += 1
        
#     else:
#         c.append(a[i])
#         i += 1
#         j += 1

# while i < len(a):
#     c.append(a[i])
#     i += 1
# while j < len(b):
#     c.append(b[j])
#     j += 1

# print(c)


#4. Finding the max element













