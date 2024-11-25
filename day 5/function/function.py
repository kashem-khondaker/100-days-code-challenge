def sum(num1 , num2):
    sum = num1 + num2
    print(sum)
    return sum

num1 = 10
num2 = 21
sum_in_function = sum(num1,num2)

def avg (num3,num4):
    avg = (num3+num4) / 2
    print(avg)
    return avg

num3 = int(input())
num4 = int(input())
avg_function = avg(num3,num4)


# calculate the number odd or even 

def Is_odd(n):
    if (n%2==0):
        print('number is jor')
    else:
        print('number is bejor')

# Is_odd(int(input('check your number : ')))
Is_odd(float(input('check your number : ')))


