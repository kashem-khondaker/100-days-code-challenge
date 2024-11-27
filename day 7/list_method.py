numbers = [12,32,45]
numbers.append(10)

print(numbers)

numbers.insert(1,99)
print(numbers)

print(numbers)
numbers.remove(12)
print(numbers)

if 8 in numbers:
    numbers.remove(8)
    print(numbers)
else:
    print("not exist")


print(numbers)
last = numbers.pop()

print(last , numbers)



numbers.append(55)
# print(numbers)
# if 5 in numbers:
#     index = numbers.index(5)
#     print(index)
# else:
#     print('not exist')
    
print(numbers)
if 32 in numbers:
    index = numbers.index(32)
    print(index)
else:
    print('not exist')
    
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

    






