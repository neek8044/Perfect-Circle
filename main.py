# Created for the Perfect Circle game on https://neal.fun/perfect-circle/
# Coded by Nick Roussis (Neek8044)
# Github: https://github.com/neek8044/Perfect-Circle
# Licensed under Apache License 2.0 (see github ^)

import pyautogui
import math
import time

# Recommended to use 3 as the SPEED factor. You might need to change the RADIUS based on your monitor resolution.
# Both of these settings work well on FHD:1920x1080
SPEED = 3
RADIUS = 494
# If on fullscreen, leave those as they are. If not, change the Y_OFFSET to around 5.6.
# No use to change the X_OFFSET unless you have a double monitor.
X_OFFSET = 0
Y_OFFSET = 0

def getX(t, rad):
    return ((pyautogui.size()[0] / 2) + math.cos(t) * rad) + Y_OFFSET

def getY(t, rad):
    return ((pyautogui.size()[1] / 2) + math.sin(t) * rad) + X_OFFSET

print('\n--> Place your cursor on the website while on fullscreen.\n\n(Ctrl+C to stop)\n')
try:
    time.sleep(3)
    for i in range(5):
        print(str(5 - i) + ' seconds left.')
        time.sleep(1)
except KeyboardInterrupt:
    print('Aborted.')
    exit()

pyautogui.moveTo(getX(0, RADIUS), getY(0, RADIUS))
pyautogui.mouseDown(button="left")
for i in range(SPEED + 2):
    t = i * math.pi / (SPEED / 2)
    pyautogui.moveTo(getX(t, RADIUS), getY(t, RADIUS), duration=0)
pyautogui.mouseUp(button='left')
