numbers = [1,2,3,1,2,3,1,2,32,21,34,65,32]

# for num in numbers:
#     numbers.sort()
#     print(num)

# print(numbers)

numbers = sorted(numbers)
# print(numbers)

numbers = list(set(numbers))
numbers = sorted(numbers)
# print(numbers)

# print(numbers[:])
# print(numbers[ : len(numbers) - 1])
# print(numbers[0:])

# revers a list in Python 
print(numbers[-1::-1])
print(numbers[::-1])

