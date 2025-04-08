
def fibonacci(n):
    
    febs = []
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        
        prev,curr = 0,1
        for _ in range(n-1):
            prev,curr = curr, prev + curr
            febs.append(curr)
            # print(curr)
    return febs    


print(fibonacci(10))