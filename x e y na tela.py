import pyautogui
from time import sleep

sleep(2)
x, y = pyautogui.position()
print(f'x = {x} e y = {y}')