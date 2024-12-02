def fun(N, a):
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # print(freq)
    removals = 0
    
    for num, count in freq.items():
        # print(f'num : {num} , count : {count}')
        if count < num:
            removals += count
        else:
            removals += count - num
    
    return removals

n = int(input()) 
array = list(map(int, input().split()))  

print(fun(n, array))
