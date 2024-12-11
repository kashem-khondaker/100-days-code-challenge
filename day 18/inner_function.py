# function is a first class object
def double_decker():
    print("starting the double decker")
    def inner_function():
        print('inside the function')
        return 3000
    return inner_function

# call the double decker
# print(double_decker())
# call inside the function
# print(double_decker()())


# we can give something function like a parameter as a function

def do_something(work):
    print('\n\nwork started!')
    work()
    print('work ended , thanks')

def work():
    print('now this is for codding time !')

# call the function
# do_something(work)
###########################################################
# again this part 

# we can call a function inside a function and we can give a parameter as a function

def double_decker2():
    print("stand in a night !")
    def inner_func():
        print('Only you can do it !')
        return 10
    return inner_func

print(double_decker2()())

def something(work):
    print('Nothing')
    work()
    print('end')
def work():
    print('handling error')

print(something(work))