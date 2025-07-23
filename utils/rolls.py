import cv2
import numpy as np
from PIL import Image, ImageEnhance
import pytesseract


CONST_ROLL_PATH = "./images/roll.jpeg"
CONST_ROLL_REGIONS = [
    (10, 20, 275, 60), # box1 for value
    (10, 105, 275, 140), # box 2 for value
    (10, 190, 275, 225), # box 3 for value
    (10, 275, 275, 310) # box 4 for value
]

CONST_ORIGINAL_ROLL_BOXES_PATH = [
    "./images/roll_box_1.png", "./images/roll_box_2.png", 
    "./images/roll_box_3.png", "./images/roll_box_4.png"
    ]

CONST_PROCESSED_ROLL_BOXES_PATH = [
    "./images/processed_roll_box_1.png", "./images/processed_roll_box_2.png",
    "./images/processed_roll_box_3.png", "./images/processed_roll_box_4.png"
]


# crop initial roll image into 4 boxes for each roll.
def cropRollBoxes(path=CONST_ROLL_PATH):
    print("Cropping roll boxes \n")
    img = Image.open(path)
    for i, box in enumerate(CONST_ROLL_REGIONS):
        cropped = img.crop(box)
        cropped.save(f"./images/roll_box_{i+1}.png")


# do preprocessing for OCR.
def enhanceBoxImage():
    print("enhancing image \n")
    counter = 0
    for img in CONST_ORIGINAL_ROLL_BOXES_PATH:
        pImg = Image.open(img).convert("L") # convert to grayscale.
        pImg = ImageEnhance.Contrast(pImg).enhance(2.0) # enhance contrast
        pImg = pImg.resize((pImg.width *2, pImg.height * 2))
        # normalise with openCV
        pImg_np = np.array(pImg)
        norm_img = np.zeros_like(pImg_np)
        pImg = cv2.normalize(pImg_np, norm_img, 0, 255, cv2.NORM_MINMAX)

        final_img = Image.fromarray(norm_img.astype(np.uint8))
        final_img.save(f"./images/processed_roll_box_{counter+1}.png")
        counter += 1
        
def readImage():
    print("reading \n")
    rolls = []
    for img in CONST_PROCESSED_ROLL_BOXES_PATH:
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=%ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        rolls.append(pytesseract.image_to_string(Image.open(img), config=custom_config).strip())
        print(pytesseract.image_to_string(Image.open(img), config=custom_config).strip())

    return rolls
        

def cropEnhanceRead():
    rolls = []
    cropRollBoxes()
    enhanceBoxImage()
    rolls = readImage()
    return rolls

# cropRollBoxes()
# enhanceBoxImage()
# readImage()