import pyautogui as ag

# find the reset button and use it as a template towards a full screenshot to detect.
def findResetButton(template_path, crkWindowImg):
    try:
        location = ag.locate(template_path, crkWindowImg, confidence=0.8)
        if location:
            return location
        else:
            return None
    except ag.ImageNotFoundException:
        return None


# should work with all resolutions given its relative to the windows fixed at 1500x1000
def moveAndClick(crkWindow, button_location):
    if button_location:
        click_x = crkWindow.left + button_location.left + button_location.width // 2
        click_y = crkWindow.top + button_location.top + button_location.height // 2
        ag.moveTo(click_x, click_y)
        ag.click()



    