def Three_sum(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)
    return result

def Multiple(num):
    result = num * 2
    print(result)
    return result

def sum_array(array1 , array2):
    sum1 = 0
    sum2 = 0
    for num in array1:
        sum1 += num
    for num in array2:
        sum2 += num
    
    Total = sum1 + sum2
    print(Total)
    return Total

array1 = [1,2,3,4,5] # sum1 = 15
array2 = [3,2,5,9,10] # sum2 = 29

sum_array(array1,array2)

def add_numbers(a, b):
    return a + b

def greet_user(name):
    return f"Hello, {name}!"

