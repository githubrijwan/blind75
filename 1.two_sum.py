def two_sum(lst,target):
    map = {}
    
    for i,n enumerate(lst):
        diff = target - n
        
        if diff in map:
            return [map[diff], i]
        map[n] = I
    return [0, 0]    
    
    
   
    
    