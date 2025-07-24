# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

from rarity import *
from rolls import *
from screenshot import *
from click import *

# winCrk = findAndResize('CookieRun')
# time.sleep(1.5)
# screenshotValues(winCrk)
# cropValueBoxes()
# high, pos = getHighRarityCount()
# print(high, pos)
high = 3
pos = [0, 1, 2]

rolls = [0, 1, 3]

print(len(set(pos) & set(rolls)) >= 2)

a = len(set(pos) & set(rolls))


# len(set(pos) & set(rolls))