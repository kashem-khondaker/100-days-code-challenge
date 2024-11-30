info = {
    "key" : "value",
    "name": "kasehm",
    "class":"learn python",
    "age" : 25,
    "is_adult": True,
    "marks": 77
}

# print(info)
print(type(info))

# access by keys
print(info['name'] , info['marks'])


# making nested dictionary 


student = {
    "name" : "Kashem Khondaker",
    "Skill" : {
        "c" : "first programming language",
        "c++" : "second programming language",
        "Python" : "third programming language"
    },
    "is_problem solver" : True
}

# print nested dictionary 
print(student)
print(f'this is Skill {student["Skill"]}\n')
print(student["Skill"]["c"])

# method in Dictionary

# myDict.Keys()             --> return all keys
# myDict.values()           --> return all values
# myDict.items()            --> return all (key, value) pair as tuples
# myDict.get("key")         --> return all key according to value
# myDict.update(newDict)    --> insert the specified items to the dictionary


print(f'\n\n{student.keys()}\n')

# we can change with type chasting like tuple , list 

print(len(student))
print(list(student.keys()))
print(student.values())
print(list(student.values()))

print(f'\n\n{student.items()}\n')

print(student["name"])
print(student.get("name"))

# why need method get in dictionary ?
# answer : if we write something that key is not exist in dictionary they it's return none if we use get method otherwise it's return error . and this is a problematic things

print(student.get("name2"))  # return none 
# print(student["name2"]) # return error