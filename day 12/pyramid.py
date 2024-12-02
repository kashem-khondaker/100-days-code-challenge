import pyautogui
import time

n = int(input())
time.sleep(5)

for i in range(1, n + 1):
    line = "#" * i  
    pyautogui.write(line , interval=0.25)  
    pyautogui.press('enter')  

