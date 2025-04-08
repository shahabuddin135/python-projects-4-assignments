
# def double(arr):
    
#     doubled = []
    
#     for num in arr:
#       num = num * 2
#       doubled.append(num)
#     return doubled

# result = double([1,2,3,4])

# print(result)



#2nd approach

def double(arr):
    
    return [num * 2 for num in arr ]

result = double([1,2,3,4])

print(result)
