# normal function in Python 

def numbers(num1, num2, num3):
    sum = num1 + num2 + num3
    # print(sum)
    return sum

three_sum = numbers(11,12,13)


# function by *args 
# that means variable numbers of parameter can be handle in function

def all_sum(*number):
    sum = 0
    for num in number:
        print(num)
        sum += num    
    return sum

total_sum = all_sum(1,11,1,232,1,2,3,4,5,6,1,2,6)
print("\ntotal_sum : " , total_sum)


