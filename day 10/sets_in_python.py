def is_palindrome(chars):
    return chars == chars[::-1]

n = int(input())  
chars = input().split()  

if is_palindrome(chars):
    print('YES')
else:
    print('NO')