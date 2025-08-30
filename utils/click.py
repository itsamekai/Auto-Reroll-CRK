import pyautogui as ag
from PIL import ImageDraw

# find the reset button and use it as a template towards a full screenshot to detect.
def findResetButton(template_path, crkWindowImg):
    try:
        location = ag.locate(template_path, crkWindowImg, confidence=0.6)
        if location:
            x, y = location.left, location.top
            width, height = location.width, location.height
            draw = ImageDraw.Draw(crkWindowImg)
            color = (255, 0, 0)
            # Draw rectangle (square)
            draw.rectangle([x, y, x + width, y + height], outline=color, width=3)  # outline only
            # crkWindowImg.save("images/reset_button.png")
            return location
        else:
            return None
    except ag.ImageNotFoundException:
        return None


# should work with all resolutions given its relative to the windows fixed at 1500x1000
def moveAndClick(crkWindow, button_location, scale_x, scale_y):
    if button_location:
        click_x = crkWindow["X"] + (button_location.left + button_location.width // 2) // scale_x
        click_y = crkWindow["Y"] + (button_location.top + button_location.height // 2) // scale_y
        ag.moveTo(click_x, click_y)
        ag.click()



    