def two_sum(lst,target):
    map = {}
    
    for i,n in enumerate(lst):
        diff = target - n
        
        if diff in map:
            return [map[diff], i]
        map[n] = i
    return [0, 0]    
    

if __name__ == "__main__":
    print(two_sum([1,4,3,5,7], 6))    
    