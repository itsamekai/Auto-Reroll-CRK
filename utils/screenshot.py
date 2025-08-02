import pyautogui as ag
import pygetwindow as gw
import time
from PIL import ImageGrab
from utils.paths import *

crkWindowsName = ['CookieRun', '쿠키런', '姜饼人王国', '薑餅人王國']

# screenshot crk window to locate reset all button.
def screenshotWindow(win):
    bbox = (win.left, win.top, win.right, win.bottom)
    return ImageGrab.grab(bbox)

# get crk window and resize. prep for screenshot.
def findAndResize():
    for win in gw.getAllTitles():
        if any(winName in win for winName in crkWindowsName):
            crWindow = gw.getWindowsWithTitle(win)
            crWindow[0].resizeTo(1500, 1000)
            print(f"Position: ({crWindow[0].left}, {crWindow[0].top})")
            print(f"Size: {crWindow[0].width}x{crWindow[0].height}")
            crWindow[0].activate()
            time.sleep(1)
            return crWindow[0]
    return None

# type of roll. CD, ATK, etc.
def screenshotRoll(win):
    # ag.screenshot(region=(win.left + 400, win.top + 455, 275, 335)).save(os.path.join(WRITABLE_IMAGE_DIR, "roll.jpeg"))
    return ag.screenshot(region=(win.left + 400, win.top + 455, 275, 335))


# cropped size is 275 x 335.
def screenshotValues(win):
    # ag.screenshot(region=(win.left + 975, win.top + 455, 105, 335)).save(os.path.join(WRITABLE_IMAGE_DIR, "roll.jpeg"))
    return ag.screenshot(region=(win.left + 975, win.top + 455, 105, 335))
    





