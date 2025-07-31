# Steps to Use
1) Turn on CRK with GPG.
2) Go to beascuit reroll page. 
3) Make sure all warning pop ups are gone. (>= 2 rolls, initial roll warnings)
4) Select lines needed (>= lines) & roll type. 
5) Press ESC to stop.

## Troubleshooting
1) If unable to detect the reset button, rescale your resolution to 1920x1080.
2) If unable to detect high rolls (i.e. constantly 0 high values), restart GPG.
3) If rolls are being read wrongly, try making use of the delay. (i.e "Cooldown" being read as "Coldown")
4) DM me on discord or @ me on discord.gg/creamery for other issues.

## TO DO
* Allow reroller to stop when rolling multiple of other same rolls, if its of high value.
* Add support for other emulators. (primarily LD.)
* Read Numbers (not that important, but nice to have?)
* Cache color_distance() results for faster read times on values

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