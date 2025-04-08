
def shorten(lst):
    
    while len(lst) > 3:
        
        removed_items = lst.pop()
    
        print(removed_items)
    
    return lst

res = shorten([1,2,3,4,5,6,7,8,9])

print(res)
    
        