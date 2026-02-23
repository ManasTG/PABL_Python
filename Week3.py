


#%% 6. Given an arr[], calc the median
# For even number, avg of two middle element

odd_arr = [90, 100, 78, 89, 67]
even_arr = [56, 67, 30, 79]
alt_even_arr = [1, 2]

def cal_median(arr):
    n = len(arr)
    arr.sort()
    
    if n % 2 == 0:
        middle_ahead = arr[n//2]
        middle_behind = arr[(n//2) - 1]
        
        med = (middle_ahead + middle_behind)/2

    else:
        med = arr[n//2]
    

    return med

print(cal_median(alt_even_arr))


#%%72. Traverse a matrix in spiral form and print it our in that format

my_mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def spiral_matrix(mat):
    n = len(mat)
    for i in range(0, n):
        
        
        
        pass

