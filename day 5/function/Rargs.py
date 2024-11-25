# def name(first,last , **additional):
#     name = f'{first} {last}'
#     # print(additional['title'])
#     return name

# favorite_name = name('Rabbil' , 'Hasan' , 'Robon')
# print(favorite_name)


# def famus_name (first,last, **addition):
#     name = f'{first} {last} '
#     for key , value in addition.items():
#         print(key,value)
#     return name

# name = famus_name(first='Taher' . last='Ali' , title='Hojur')
# print(name)


def name(first, last, **additional):
    name = f'{first} {last}'
    # Uncomment this line if you want to access specific additional data
    # print(additional['title'])
    return name

# Corrected call with keyword argument for **additional
favorite_name = name('Rabbil', 'Hasan', title='Robon')
print(favorite_name)

def famus_name(first, last, **addition):
    name = f'{first} {last}'
    for key, value in addition.items():
        print(key, value)
    return name

# Corrected function call with comma instead of dot
famous_name = famus_name(first='Taher', last='Ali', title='Hojur')
print(famous_name)
