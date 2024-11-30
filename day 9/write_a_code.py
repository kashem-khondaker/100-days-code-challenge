def is_palindrome(s):
    return s == s[::-1]  

user_input = input().strip()

reversed_input = str(int(user_input[::-1]))  

if is_palindrome(user_input):
    print(reversed_input)
    print("YES")
else:
    print(reversed_input)
    print("NO")
