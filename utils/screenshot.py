import pyautogui as ag
import pygetwindow as gw
import time
from PIL import ImageGrab
from utils.paths import *

crkWindowsName = ['CookieRun', '쿠키런', '姜饼人王国', '薑餅人王國', 'LDPlayer', 'CRKROLL']
CONST_GPG_WIN_NAMES = ['CookieRun', '쿠키런', '姜饼人王国', '薑餅人王國']
CONST_LDPLAYER_WIN_NAME = ['LDPlayer']
CONST_MUMU_WIN_NAME = ['CRKROLL']

# regions for Google Play Games
gpg_value_region = (975, 455, 105, 335)
gpg_roll_region = (400, 455, 275, 335)

# region for LDPlayer.
ldp_value_region = (940, 470, 105, 335)
ldp_roll_region = (395, 470, 275, 335)

# region for Mumu.
mumu_value_region = (975, 480, 105, 335)
mumu_roll_region = (400, 480, 275, 335)

EMU_REGIONS = {
    "LDPlayer": (ldp_value_region, ldp_roll_region),
    "GPG": (gpg_value_region, gpg_roll_region),
    "Mumu": (mumu_value_region, mumu_roll_region)
}

# screenshot crk window to locate reset all button.
def screenshotWindow(win):
    bbox = (win.left, win.top, win.right, win.bottom)
    # ImageGrab.grab(bbox).save(os.path.join(WRITABLE_IMAGE_DIR, "crkWindows.jpeg"))
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
            # partial check.
            emu = (
                'GPG' if any(name in win for name in CONST_GPG_WIN_NAMES)
                else 'LDPlayer' if any(name in win for name in CONST_LDPLAYER_WIN_NAME)
                else 'Mumu' if any(name in win for name in CONST_MUMU_WIN_NAME)
                else None
            )
            time.sleep(1)
            
            return crWindow[0], emu
    return None, None

# type of roll. CD, ATK, etc.
# makes use of the emu counts to determine, since future would further support more
def screenshotRoll(win, emu):
    x, y, width, height = EMU_REGIONS[emu][1]
    # ag.screenshot(region=(win.left + x, win.top + y, width, height)).save(os.path.join(WRITABLE_IMAGE_DIR, "roll.jpeg"))
    return ag.screenshot(region=(win.left + x, win.top + y, width, height))


# cropped size is 275 x 335.
def screenshotValues(win, emu):
    x, y, width, height = EMU_REGIONS[emu][0]
    # ag.screenshot(region=(win.left + x, win.top + y, width, height)).save(os.path.join(WRITABLE_IMAGE_DIR, "value.jpeg"))
    return ag.screenshot(region=(win.left + x, win.top + y, width, height))
    





