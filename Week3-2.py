#1. Given an arr[], calc the median

my_arr = [90, 100, 78, 89, 67]

def cal_median(arr):
    n = len(arr)
    med = 0    
    arr.sort()
    
    if n % 2 == 0:
        med = arr
        
        # return med
    else:
        pass

    
    
    return med

print(cal_median(my_arr))