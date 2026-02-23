


#%% 9. sort without using any space and function
nums = [2,0,2,1,1,0]
def sort_color(num):
    low = 0
    mid = 0
    high = len(num) - 1
    
    while mid <= high:
        if num[mid] == 0:
            num[low], num[mid] = num[mid], num[low]
            low += 1
            mid += 1
        elif num[mid] == 1:
            mid += 1
        else:
            num[mid], num[high] = num[high], num[mid]
            high -= 1
                
            
    return num
print(sort_color(nums))