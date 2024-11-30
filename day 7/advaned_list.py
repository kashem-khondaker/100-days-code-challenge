numbers = [45,12,32,11,22,33,44,55,66,77,88,99]
odd = []
even = []
# for num in numbers:
#     if num % 2 == 1 and num % 5 == 0 :
#         odd.append(num)
#     else:
#         even.append(num)

print("printing numbers" , numbers)

odd_nums = [num for num in numbers if num % 2 == 1]
print("printing odd_nums",odd_nums)
