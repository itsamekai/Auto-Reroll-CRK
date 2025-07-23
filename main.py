from utils.rarity import *
from utils.rolls import *
from utils.screenshot import *
from utils.click import *

AMP_BUFF = 'AmplifyBuff'
DR_BYPASS = 'DMGResistBypass'
DMG_RESIST = 'DMGResist'
CRIT_RATE = 'CRIT%'
ATK = 'ATK'
HP = 'HP'
DEF = 'DEF'
ATTACK_SPEED = 'ATKSPD'
COOLDOWN = 'Cooldown'
DEBUFF_RESIST = 'DebuffResist'

# elemental, to add  
DARK_DMG = 'DarkDMG'



crkWin = findAndResize('CookieRun')
count = []
rolled = []
if crkWin:
    screenshotRoll(crkWin)                  # screenshot the rolls
    iterations = 0
    while iterations != 10:
        rolls = []
        moveAndClick(crkWin)                # move to reset all and click once
        time.sleep(1)
        screenshotValues(crkWin)            # screenshot the value of rolls first. determine color
        cropValueBoxes()                    # crop the value of rolls to boxes
        high_count = getHighRarityCount()   # sort by color density to return

        # only go here if high_count is >=2, temp check all
        screenshotRoll(crkWin)
        rolls = cropEnhanceRead()
        rolled.append(rolls)
        count.append(high_count)
        iterations += 1

print(count)
print(rolled)