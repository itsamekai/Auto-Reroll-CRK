from PIL import Image
from utils.paths import *


CONST_ORANGE_RGBA = (255, 120, 0) # orange RGBA for orange rarity
CONST_PURPLE_RGBA = (184, 61, 255) # purple RGBA for purple rarity
CONST_VALUE_REGIONS = [
    (0, 20, 100, 60), # box 1 for value
    (0, 105, 100, 140), # box 2 for value
    (0, 190, 100, 225), # box 3 for value
    (0, 270, 100, 310) # box 4 for value
]


# crop the value image into 4 different boxes with their own respective values.
def cropValueBoxes(valueImg, tainted):
    croppedBoxes = []
    if tainted: # if tainted biscuits, start from n=1 since 1st roll is fixed.
        for box in CONST_VALUE_REGIONS[1:]:
            croppedBoxes.append(valueImg.crop(box))
    else:
        for box in CONST_VALUE_REGIONS:
            croppedBoxes.append(valueImg.crop(box))
            
    return croppedBoxes


def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1[:3], c2))


# min 0. max 4. increment per purple / orange
def getHighRarityCount(boxes, orange_bool): 
    # holds the no. of high rolls
    high_count = 0
    pos = []
    colors = [CONST_ORANGE_RGBA] if orange_bool else [CONST_ORANGE_RGBA, CONST_PURPLE_RGBA] # check only orange if true

    for i, img in enumerate(boxes):
        valueImage = img.convert("RGBA")    
        pixels = list(valueImage.getdata())
        
        high_pixel_count = sum(
            1 for px in pixels
            if any(color_distance(px, color) < 900 for color in colors)
        )

        density = high_pixel_count / len(valueImage.getdata())
        # print(f"img: {img}, density: {density}")
        if density > 0.02:
            high_count += 1
            pos.append(i)
             
    return high_count, pos






