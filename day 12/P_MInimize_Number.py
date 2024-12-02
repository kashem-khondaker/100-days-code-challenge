n = int(input())
array = list(map(int, input().split()))

max_number = 2147483647
for num in array:
    count = 0
    
    while num % 2 == 0:
        num //= 2
        count += 1
    max_number = min(max_number, count)

print(max_number)
