import time
from utils.screenshot import *
from utils.click import *
from utils.rolls import *
from utils.rarity import *
from utils.paths import resource_path
from handler.state import *

CONST_RESET_BUTTON_PATH = resource_path("template/reset_button.png")

def run_task(roll_type, line_count, tainted_bool, delay, tesseractAPI, log):
    counter = 1

    # init crk window from gpg
    crkWin = findAndResize()
    if not crkWin:
        log("CRK window not found. Open GPG.")
        set_running(False)
        return
    
    # get the reset button location coordinates
    crkImage = screenshotWindow(crkWin)
    resetLoc = findResetButton(CONST_RESET_BUTTON_PATH, crkImage)
    print(f"reset button location: {resetLoc}")

    if not isinstance(resetLoc, tuple):
        log("Reset button not found. Check UI.")
        set_running(False)
        return
    
    else:
        log("Reset button found.")
        log("Starting auto reroll.")

    while is_running():
        start = time.time()
        moveAndClick(crkWin, resetLoc) # start click
        time.sleep(1.14 + float(delay))
        value_screenshot = screenshotValues(crkWin)
        cropped = cropValueBoxes(value_screenshot, tainted_bool)
        high_count, pos = getHighRarityCount(cropped)
        
        # check if the amount of purple / orange rolls is >= the no. of lines picked
        if (high_count >= int(line_count)):
            roll_screenshot = screenshotRoll(crkWin)
            rollResult, rolled = cropEnhanceRead(pos, roll_type, line_count, roll_screenshot, tainted_bool, tesseractAPI)
            if rollResult:
                elapsed = round(time.time() - start, 2)
                log(f"Successfully rolled. Total: {counter} rolls done. {elapsed} time taken.")
                break
            else:
                elapsed = round(time.time() - start, 2)
                log(f"Roll {counter}: {high_count} high values but wrong rolls - {rolled}. {elapsed} time taken.")
                counter+= 1
        else:
            elapsed = round(time.time() - start, 2) 
            log(f"Roll {counter}: {high_count} high values. {elapsed}s time taken.")
            counter+= 1

    log("auto reroll stopped.")
    set_running(False)