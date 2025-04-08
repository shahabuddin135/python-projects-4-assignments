def summ_all(arr):
    
    total = 0
    
    for num in range(len(arr)):
        total += arr[num]
    
    return total

result = summ_all([1,2,3,4])

print(result)
    