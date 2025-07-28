import cv2
import numpy as np
from PIL import Image, ImageEnhance
import pytesseract
from utils.paths import *


CONST_ROLL_REGIONS = [
    (10, 20, 275, 60), # box1 for value
    (10, 105, 275, 140), # box 2 for value
    (10, 190, 275, 225), # box 3 for value
    (10, 275, 275, 310) # box 4 for value
]

# crop initial roll image into 4 boxes for each roll.
def cropRollBoxes(rollImg):
    croppedBoxes = []
    for box in CONST_ROLL_REGIONS:
        croppedBoxes.append(rollImg.crop(box))
    return croppedBoxes


# do preprocessing for OCR.
def enhanceBoxImageAndRead(pos, rollType, line_count, valueImg):
    print("enhancing image \n")
    counter = 0
    rolls = []
    rollPos = []
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=%ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i, img in enumerate(valueImg):
        pImg = img.convert("L") # convert to grayscale.
        pImg = ImageEnhance.Contrast(pImg).enhance(2.0) # enhance contrast
        pImg = pImg.resize((pImg.width *2, pImg.height * 2))
        # normalise with openCV
        pImg_np = np.array(pImg)
        norm_img = np.zeros_like(pImg_np)
        pImg = cv2.normalize(pImg_np, norm_img, 0, 255, cv2.NORM_MINMAX)

        final_img = Image.fromarray(norm_img.astype(np.uint8))
        # final_img.save(CONST_PROCESSED_ROLL_BOXES_PATH[i])
        print(f"reading roll {i + 1}:")
        rolled = pytesseract.image_to_string(img, config=custom_config).strip()
        if rolled == rollType:
            rollPos.append(i)
        rolls.append(rolled) # just for clarity to see all rolls
    
    print(rolls)
    print(f"value pos: {pos} -- roll pos: {rollPos}") 
    # check positional values; pos[] array returns the position of high values.
    # match the positional values with the positional rolls & check if >= line count (determined by user)
    if len(set(pos) & set(rollPos)) >= int(line_count):
        return True, rolls
    else:
        return False, rolls


def cropEnhanceRead(pos, rollType, lineCount, value_screenshot):
    cropped = cropRollBoxes(value_screenshot)
    return enhanceBoxImageAndRead(pos, rollType, lineCount, cropped)