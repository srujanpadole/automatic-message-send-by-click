import pyautogui
import time
time.sleep(1)

count =0
while count<=50:
    pyautogui.typewrite("hey"+str(count))
    pyautogui.press("enter")
    count+=1
    