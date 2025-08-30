from utils.paths import *


CONST_ORANGE_RGBA = (236, 131, 50) # orange RGBA for orange rarity
CONST_PURPLE_RGBA = (170, 70, 246) # purple RGBA for purple rarity
CONST_CRK_VALUE_REGIONS = [
    (0, 25, 160, 90), # box 1 for value
    (0, 145, 160, 210), # box 2 for value
    (0, 265, 160, 330), # box 3 for value
    (0, 385, 160, 450) # box 4 for value
]

# crop the value image into 4 different boxes with their own respective values.
def cropValueBoxes(valueImg, tainted):
    croppedBoxes = []
    crop_region = CONST_CRK_VALUE_REGIONS
    if tainted: # if tainted biscuits, start from n=1 since 1st roll is fixed.
        for box in crop_region[1:]:
            croppedBoxes.append(valueImg.crop(box))
    else:
        for box in crop_region:
            croppedBoxes.append(valueImg.crop(box))
            # valueImg.crop(box).save(f"images/value_box_{counter}.png")
            
    return croppedBoxes


def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1[:3], c2))


# min 0. max 4. increment per purple / orange
def getHighRarityCount(boxes, orange_bool): 
    # holds the no. of high rolls
    high_count = 0
    pos = []
    colors = [CONST_ORANGE_RGBA] if orange_bool else [CONST_ORANGE_RGBA, CONST_PURPLE_RGBA] # check only orange if true
    # start = time.time()
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
    # print(f"compute color time: {time.time() - start}")
    return high_count, pos






