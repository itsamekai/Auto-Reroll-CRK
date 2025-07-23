import pyautogui as ag
import pygetwindow as gw
import time
from PIL import Image, ImageGrab

CONST_VALUE_PATH = "./images/values.jpeg"
CONST_ROLL_PATH = "./images/roll.jpeg"


# get crk window and resize. prep for screenshot.
def findAndResize(title):
    for win in gw.getAllTitles():
        if title in win:
            crWindow = gw.getWindowsWithTitle(win)
            crWindow[0].resizeTo(1500, 1000)
            print(f"Position: ({crWindow[0].left}, {crWindow[0].top})")
            print(f"Size: {crWindow[0].width}x{crWindow[0].height}")
            crWindow[0].activate()
            time.sleep(0.05)
            return crWindow[0]
    return None

# type of roll. CD, ATK, etc.
def screenshotRoll(win):
    # time.sleep(0.05)
    img = ag.screenshot(region=(win.left + 400, win.top + 455, 275, 335))
    img.save("roll.jpeg")


# cropped size is 275 x 335.
def screenshotValues(win):
    img = ag.screenshot(region=(win.left + 975, win.top + 455, 105, 335))
    img.save(CONST_VALUE_PATH)


win = findAndResize('CookieRun')
# screenshotRoll(win)
screenshotValues(win)





