import pyautogui
import time

n = int(input())
time.sleep(5)

for i in range(1, n + 1):
    line = "#" * i  
    pyautogui.write(line)  
    pyautogui.press('enter')  

def sum_all(*args):
    return sum(args)

# Usage
print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5, 6, 7, 8))  # Output: 30

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Usage
print_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
