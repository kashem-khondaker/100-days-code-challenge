# string is immutable 
# it's a sequence of character
# we can slice it
# we can access it's index but by using index we can't change it




name = 'Kashem Khondaker'
name2 = "kashem khondaker"
name3 = """
        this is 
        multiline string.
"""

# print(name)
# print(name2)
# print(name3)


# we can escape something in string as for example

# name = 'kashem's khondaker'

# solve this problem by this weya 


name = 'kashem\'s khondaker '  # escape 
# print(name)


print(name[:len(name)])

print(name[1:5])
print(name[-4])
print(name[::-1])


