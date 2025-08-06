import cv2
import numpy as np
from PIL import Image, ImageEnhance
from utils.paths import *
from collections import Counter

CONST_GPG_ROLL_REGIONS = [
    (10, 15, 275, 65),    
    (10, 100, 275, 150),   
    (10, 185, 275, 235),  
    (10, 270, 275, 320)  
]

CONST_LDPLAYER_ROLL_REGIONS = [
    (0, 15, 275, 65),    
    (0, 100, 275, 150),   
    (0, 185, 275, 235),  
    (0, 270, 275, 320)  
]

CONST_MUMU_ROLL_REGIONS = [
    (10, 15, 275, 65),    
    (10, 100, 275, 150),  
    (10, 185, 275, 235),  
    (10, 270, 275, 320)  
]


EMU_CROPPED_REGIONS = {
    "LDPlayer": CONST_LDPLAYER_ROLL_REGIONS,
    "GPG": CONST_GPG_ROLL_REGIONS,
    "Mumu": CONST_MUMU_ROLL_REGIONS
}

# crop initial roll image into 4 boxes for each roll.
def cropRollBoxes(emu, rollImg, tainted):
    crop_region = EMU_CROPPED_REGIONS[emu]
    croppedBoxes = []
    if tainted:
        for box in crop_region[1:]:
            croppedBoxes.append(rollImg.crop(box))
    else:
        for box in crop_region:
            croppedBoxes.append(rollImg.crop(box))
            # rollImg.crop(box).save(os.path.join(WRITABLE_IMAGE_DIR, f"cropped_box{counter}.jpeg"))
    return croppedBoxes


def preprocessImage(img):
    img = img.convert("L")
    img = ImageEnhance.Contrast(img).enhance(2.0)
    img = img.resize((img.width * 2, img.height * 2))

    np_img = np.array(img)
    norm_img = cv2.normalize(np_img, None, 0, 255, cv2.NORM_MINMAX)
    # Image.fromarray(norm_img.astype(np.uint8)).save(os.path.join(WRITABLE_IMAGE_DIR, f"processed_cropped_box.jpeg"))

    return Image.fromarray(norm_img.astype(np.uint8))


# do preprocessing for OCR.
def enhanceBoxImageAndRead(pos, rollType, line_count, chopsticks, valueImg, tesserectAPI):
    finalRolls = []
    rolled = []
    processed = [preprocessImage(img) for img in valueImg] # pre-process all cropped images

    for i, processedImg in enumerate(processed):
        tesserectAPI.SetImage(processedImg)
        read = tesserectAPI.GetUTF8Text().strip().replace(" ", "")
        rolled.append(tuple((read, i))) # i.e. [('Cooldown'), 0], [<roll>, <pos>]
        finalRolls.append(read) 

    # unpacks the tuple as roll and idx and puts it in a new temp list.
    # checks the temp list if the roll is in the choosen array and pos in position array
    # get the frequency and return if n amt >= count
    matched = [roll for roll, idx in rolled if roll in rollType and idx in pos] 
    print(f"pos: {pos} \nrolled: {rolled}\nmatched: {matched}")
    freq = Counter(matched)

    uniqueRolls = any(amt >= int(line_count) for amt in freq.values()) # covers unique rolls where >= line_count
    chopsticks = len(matched) >= 2 and len(freq) >= 2 # this covers 1-1 or 1-2, etc
    found = uniqueRolls or chopsticks
    print(f"found match? - {found}")
    print(finalRolls)
    return found, finalRolls # check if n amt >= line_count (determined by user)


def cropEnhanceRead(emu, pos, rollType, lineCount, value_screenshot, tainted, chopsticks, tesseractAPI):
    cropped = cropRollBoxes(emu, value_screenshot, tainted)
    return enhanceBoxImageAndRead(pos, rollType, lineCount, chopsticks, cropped, tesseractAPI)