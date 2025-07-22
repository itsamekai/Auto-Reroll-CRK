1. pixel detection for static words. add per stat.
2. check 1) first. if it passes what we are checking for, check for color to determine roll rarity


fixed screenshotting
1. force resize of the app to a specific resolution.
	- make use of pygetwindow ; https://pypi.org/project/PyGetWindow/
	

2. click reroll. 

3. set up pixel matching / detection 
	- check for stat -> check number colors -> check actual numbers if exceed
	1) manually find pixel coordinates for:
		- stat specific pixels (cd, bypass, etc)
		- colors at number
		- OCR? if not pixel density for numbers.

4) return accordingly. or reroll again.


automation for clicking - pyautogui https://pypi.org/project/PyGetWindow/
possible OCR for numbers - pytesseract https://pypi.org/project/pytesseract/
