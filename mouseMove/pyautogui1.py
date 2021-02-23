import pyautogui
x = pyautogui.size()
y = pyautogui.position()
print(x)
print(y)
pyautogui.moveTo(x=0,y=0,duration=4)
