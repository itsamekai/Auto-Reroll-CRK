# Features 
1) Allows picking of **multiple rolls**. i.e if CD, ATK are picked and at least 2 lines, it will stop when it hits either 2 lines of CD or 2 lines of ATK. Doesn't work for 1/1. **(no limit to how many you pick!)**
2) Tainted beascuit support.
3) Orange rolls only option; this means it only stops if you roll _n_ amount of orange rolls. Purple does not count.
4) Supports Google Play Games only. (please be patient for other emulators!) 

## Languages Available
If you wish to contribute towards the project by translating, please message me on discord!

- 🇹🇭 ไทย (Thai)
- 🇫🇷 Français (French)
- 🇹🇼 繁體中文 (Traditional Chinese) 


## Steps to Use
1) Turn on CRK with GPG.
2) Go to beascuit reroll page. 
3) Make sure all warning pop ups are gone. (>= 2 rolls, initial roll warnings)
4) Select lines needed (>= lines) & roll type(s). 
5) Press ESC to stop.

## Troubleshooting
1) If unable to detect the reset button, rescale your resolution to 1920x1080, or put in your main monitor (if using more than 1). 
2) If unable to detect high rolls (i.e. constantly 0 high values), restart GPG.
3) If rolls are being read wrongly, try making use of the delay. Do note that false positives does happen, but it is _rare_.(i.e "Cooldown" being read as "Coldown")
4) DM me on discord or @ me on discord.gg/creamery for other issues.

## TO DO
* Add support for other emulators. (primarily LD.)
* Cache color_distance() results for faster read times on values (each computation is 0.02s~ atm)
* Attempt color density calculations without waiting for the glare 

## Development

1. Create a venv and install the requirements:
```
bash
py -m venv venv
source venv/bin/activate # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. run main.py to launch UI.
```
py main.py
```

## Special Thanks to Our Translators!

Thank you to the following individuals for contributing their time and effort to make this project accessible in multiple languages:

- 🇹🇭 **ไทย (Thai)**: Bushy - @bushy2018
- 🇫🇷 **Français (French)**: Luz - @luzushi
- 🇹🇼 **繁體中文 (Traditional Chinese)**: JackyKuo (my goat)