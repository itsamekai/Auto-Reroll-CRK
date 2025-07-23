from PIL import Image
import pyautogui as ag

CONST_ORANGE_RGBA = (255, 120, 0) # orange RGBA for orange rarity
CONST_PURPLE_RGBA = (184, 61, 255) # purple RGBA for purple rarity
CONST_VALUE_PATH = "./images/values.jpeg"
CONST_VALUE_REGIONS = [
    (0, 20, 100, 60), # box 1 for value
    (0, 105, 100, 140), # box 2 for value
    (0, 190, 100, 225), # box 3 for value
    (0, 270, 100, 310) # box 4 for value
]

CONST_VALUE_BOXES_PATH = [
    "./images/value_box_1.png", "./images/value_box_2.png", 
    "./images/value_box_3.png", "./images/value_box_4.png"
    ]


# crop the value image into 4 different boxes with their own respective values.
def cropValueBoxes(path=CONST_VALUE_PATH):
    img = Image.open(path)
    for i, box in enumerate(CONST_VALUE_REGIONS):
        cropped = img.crop(box)
        cropped.save(f"./images/value_box_{i+1}.png")


def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1[:3], c2))


# min 0. max 4. increment per purple / orange
def getHighRarityCount(): 
    # holds the no. of high rolls   
    high_count = 0
    for img in CONST_VALUE_BOXES_PATH:
        valueImage = Image.open(img).convert("RGBA")    
        pixels = list(valueImage.getdata())
        
        high_pixel_count = sum(
            1 for px in pixels
            if any(color_distance(px, color) < 900 for color in (CONST_ORANGE_RGBA, CONST_PURPLE_RGBA))
        )

        density = high_pixel_count / len(valueImage.getdata())
        # print(f"img: {img}, density: {density}")
        if density > 0.02:
            high_count += 1
             
    return high_count



# cropValueBoxes()
# high = getHighRarityCount()
# print(high)




