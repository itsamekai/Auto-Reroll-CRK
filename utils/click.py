import pyautogui as ag
import time
# from screenshot import *

# harcoded the incremental values to align with 'Reset All'
# should work with all resolutions given its relative to the windows fixed at 1500x1000
def moveAndClick(crkWindow):
    abs_x = crkWindow.left + 850
    abs_y = crkWindow.top + 900
    ag.moveTo(abs_x, abs_y, 0.5)
    ag.click()

    