# x = 25
# y = 26
# if(x>y) :
#     print('True')
#     if(x*2 == 50):
#         print('True')
# else:
#     print('Not True')

# for loop in Python

#          for item in sequence:
    #           code to execute
    
    
# basic loop in a array
    
# fruits = ["apple" , "banana" , "cherry"]
# print(type(fruits))

# for fruit in fruits:
#     print(fruit)


# Looping over a range()



print("Looping value with range()\n")
for value in range(10):
    print(value)


# Looping over a range() with advance


print("\nLooping value advanced with range() \n")    
for value in range(1,11,2):
    print(value)



# nested for LOOPS in Python

print("\nNested FOR loop Python\n")
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for num in row:
        print(num , end=" ")
    print()

# Loop with if , else condition 

print("\nLoop with condition\n")

for i in range(5):
    print(i)
else:
    print("Loop completed!")
