x = 25
y = 26

if(x>y) :
    print('True')
    if(x*2 == 50):
        print('True')
else:
    print('Not True')

# for loop in Python

#          for item in sequence:
#               code to execute
    
    
# basic loop in a array
    
fruits = ["apple" , "banana" , "cherry"]
print(type(fruits))

for fruit in fruits:
    print(fruit)


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

print("\nanother conditional for loop in Python\n")

for i in range(10):
    if(i%2==0):
        print(i)
    else:
        continue

print("\npractice with some if else condition in for loop\n")

for i in range(20):
    if i <= 10:
        if i % 2 == 0 and i != 0:
            print(f"i = {i}", end="\n")  # Print i when i is even and not 0
    else:
        print("Fuck you!")
        break  # Break the loop when i > 10

# print their index with value

for i in range(20):
    if i <= 10:
        if i % 2 == 0 and i != 0:
            print(f'Index = {i}, Value = {i}', end="\n")
    else:
        print(f'Index = {i}, Value = Fuck you!')
        break

