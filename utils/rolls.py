import cv2
import numpy as np
from PIL import Image, ImageEnhance
from utils.paths import *
from collections import Counter

CONST_GPG_ROLL_REGIONS = [
    (10, 20, 275, 60), # box1 for value
    (10, 105, 275, 140), # box 2 for value
    (10, 190, 275, 225), # box 3 for value
    (10, 275, 275, 310) # box 4 for value
]

CONST_LDPLAYER_ROLL_REGIONS = [
    (3, 23, 275, 60), # box1 for value
    (3, 108, 275, 140), # box 2 for value
    (3, 192, 275, 225), # box 3 for value
    (3, 275, 275, 310) # box 4 for value
]

CONST_MUMU_ROLL_REGIONS = [
    (10, 25, 275, 63),    
    (10, 100, 275, 150),  
    (10, 185, 275, 235),  
    (10, 275, 275, 325)  
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

    return Image.fromarray(norm_img.astype(np.uint8))


# do preprocessing for OCR.
def enhanceBoxImageAndRead(pos, rollType, line_count, valueImg, tesserectAPI):
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

    print(finalRolls)
    return any(amt >= int(line_count) for amt in freq.values()), finalRolls # check if n amt >= line_count (determined by user)


def cropEnhanceRead(emu, pos, rollType, lineCount, value_screenshot, tainted, tesseractAPI):
    cropped = cropRollBoxes(emu, value_screenshot, tainted)
    return enhanceBoxImageAndRead(pos, rollType, lineCount, cropped, tesseractAPI)