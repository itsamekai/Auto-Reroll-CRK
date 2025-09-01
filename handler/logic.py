import time
from utils.screenshot import *
from utils.click import *
from utils.rolls import *
from utils.rarity import *
from utils.paths import resource_path
from handler.state import *


CONST_RESET_BUTTON_PATH = resource_path("template/reset_button.png")


def run_task(roll_type, line_count, orange_bool, tainted_bool, chopsticks_bool, roll_amount, delay, tesseractAPI, log):
    counter = 1
    set_translator_language()
    translator = get_translator()
    
    # init crk window from gpg
    crkWin, emu = findAndResize()
    # print(f"emulator: {emu}")
    if not crkWin:
        log(translator.text("crk_not_found"))
        set_running(False)
        return
    
    # get the reset button location coordinates
    crkImage = screenshotWindow(crkWin)
    resetLoc = findResetButton(CONST_RESET_BUTTON_PATH, crkImage)
    print(f"reset button location: {resetLoc}")

    if not isinstance(resetLoc, tuple):
        log(translator.text("reset_btn_not_found"))
        set_running(False)
        return  
    
    else:
        log(translator.text("reset_btn_found"))
        log(translator.text("reroll_start")) 
        log(f"Emulator: {emu}")
        log(translator.text("selected_rolls", roll_type=", ".join([translator.text(roll) for roll in roll_type])))
        log(translator.text("selected_amount", roll_amount=roll_amount))
        if orange_bool:
            log(translator.text("orange_warning"))

    # no. of times to roll
    roll_limit = int(roll_amount)

    while is_running():
        if roll_limit > 0 and counter > roll_limit:
            break
        start = time.time()
        moveAndClick(crkWin, resetLoc) # start click
        time.sleep(1.14 + float(delay))
        value_screenshot = screenshotValues(crkWin, emu)
        cropped = cropValueBoxes(value_screenshot, tainted_bool, emu)
        high_count, pos = getHighRarityCount(cropped, orange_bool)

        # check if the amount of purple / orange rolls is >= the no. of lines picked
        if (high_count >= int(line_count)):
            roll_screenshot = screenshotRoll(crkWin, emu)
            rollResult, rolled = cropEnhanceRead(emu, pos, roll_type, line_count, roll_screenshot, tainted_bool, chopsticks_bool, tesseractAPI)
            if rollResult:
                elapsed = round(time.time() - start, 2)
                log(translator.text("roll_success", counter=counter, elapsed=elapsed))
                break
            else:
                translated = translator.translate_rolls(rolled)
                elapsed = round(time.time() - start, 2)
                log(translator.text("roll_partial_success", counter=counter, high_count=high_count, rolled=translated, elapsed=elapsed))
                counter+= 1
        else:
            elapsed = round(time.time() - start, 2)
            log(translator.text("roll_fail", counter=counter, high_count=high_count, elapsed=elapsed))
            counter+= 1

    log(translator.text("reroll_stop", roll_amount=counter))
    set_running(False)