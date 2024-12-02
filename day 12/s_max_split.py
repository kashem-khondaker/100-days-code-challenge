
s = input().strip()

balance = 0  
count = 0 
result = []  
index = 0  

for i, char in enumerate(s):
    if char == 'L':
        balance += 1
    elif char == 'R':
        balance -= 1

    if balance == 0:
        count += 1
        result.append(s[index:i+1])
        index = i + 1  

print(count)
for sub in result:
    print(sub)

























