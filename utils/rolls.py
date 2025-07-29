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
def cropRollBoxes(rollImg, tainted):
    croppedBoxes = []
    if tainted:
        for box in CONST_ROLL_REGIONS[1:]:
            croppedBoxes.append(rollImg.crop(box))
    else:
        for box in CONST_ROLL_REGIONS:
            croppedBoxes.append(rollImg.crop(box))
    return croppedBoxes


def preprocessImage(img):
    img = img.convert("L")
    img = ImageEnhance.Contrast(img).enhance(2.0)
    img = img.resize((img.width * 2, img.height * 2))

    np_img = np.array(img)
    norm_img = cv2.normalize(np_img, None, 0, 255, cv2.NORM_MINMAX)

    return Image.fromarray(norm_img.astype(np.uint8))


# do preprocessing for OCR.
def enhanceBoxImageAndRead(pos, rollType, line_count, valueImg):
    print("enhancing image \n")
    rolls = []
    rollPos = []
    processed = [preprocessImage(img) for img in valueImg] # pre-process all cropped images
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=%ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i, processedImg in enumerate(processed):
        print(f"reading roll {i + 1}:")
        rolled = pytesseract.image_to_string(processedImg, config=custom_config).strip()
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


def cropEnhanceRead(pos, rollType, lineCount, value_screenshot, tainted):
    cropped = cropRollBoxes(value_screenshot, tainted)
    return enhanceBoxImageAndRead(pos, rollType, lineCount, cropped)