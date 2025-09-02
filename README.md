# Auto Reroll
If this reroller has helped you greatly, feel free to tip me so I can buy a coffee, I appreciate any amount!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/boonkai/tip)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/creamery)




# Features 
The Beascuit Auto Reroller has lots to offer, and should suit all your needs! See below.

## Multiple Rolls
Allows picking of **multiple rolls**. It will stop when you roll at laest _n_ number of lines of the selected roll(s).

Example: If CD, ATK are picked and at least 2 lines, it will stop when it hits either at least 2 lines of CD or ATK. Doesn't work for 1/1. **(no limit to how many you pick!)**

## Chopsticks
it will stop if you high roll _one of each_ selected rolls. (minimum _n_ number of rolls, player determined.) Alternatively also works if its 1/1, 1/2, 1/3, 1/1/1, 1/1/1/1, etc. 

Example:
If you picked the rolls: CD, ATK, CRIT, ATKSPD and it rolled to 1 line of ATK, 1 line of ATKSPD, it stops.
Possible combinations: 1/1, 1/2, 1/3, 1/1/1, 1/1/1/1.

If you can read code, this should explain it:
```
chopsticks = len(matched) >= 2 and len(freq) >= 2 # this covers 1-1 or 1-2, etc
```

Enable this option if you just want a combination of any possible choosen rolls!

## Tainted Beascuit Support
Allows you to roll Tainted Beascuits as well.

## Orange Rolls Only
Orange rolls only option! 
It only stops if you roll _n_ amount of orange rolls. Purple roll does not count.

Try not to pick >=3 rolls when using this, as it can be quite unrealistic probability wise. Unless you're using Chopsticks function with this, then it _may not_ be too bad. 

## Limit No. of Rolls
You can choose how many times you wish to roll!

If you choose 50, it will stop once it hits 50 rolls. Alternatively you can always press ESC to stop rolling. 

## Steps to Use
Different emulators has its own different ways to run. **GPG is the most consistent!**

1) Go to beascuit reroll page.
2) Remove the warning pop ups, i.e. >= 3 rolls, and the initial roll warning.
3) Select the options as needed.
4) ESC to stop if you wish to stop it midway through.

For the type of emulator you are using, please see below.

### Google Play Games
1) Turn on Google Play Games. 
2) Use the emulator's full screen (F11) or press the arrow key on the left side menu to full screen.
3) ALT TAB to the Auto Reroller.
4) Start the Reroller. 

### LDPlayer
1) Ensure that the extra icons on the right hand side is expanded. You can expand this icon menu on the top right of the emulator.
2) Rename your LDPlayer to its default name: 'LDPlayer', without the ' 

### MuMuPlayer
1) Ensure your resolution is at 1920x1080. I have not tested other resolutions as I do not have access to them, but it should work!
2) Rename your CRK emulator to 'CRKROLL' do not add the ' in!





## Troubleshooting
1) If unable to detect the reset button, rescale your resolution to 1920x1080, or put in your main monitor (if using more than 1). 
2) If unable to detect high rolls (i.e. constantly 0 high values), restart GPG.
3) If rolls are being read wrongly, try making use of the delay. Do note that false positives does happen, but it is _rare_.(i.e "Cooldown" being read as "Coldown")
4) Make sure that the AutoReroll application is saved in a file path of ONLY english characters to prevent any UTF-8 errors.
4) DM me on discord or @ me on discord.gg/creamery for other issues.



## Languages Available
For now, the languages available should be more than sufficient, unless requested by popular demand. I will reach out to the community if translations are needed! Thank you.

- 🇬🇧 English  
- 🇰🇷 한국인 (Korean)  
- 🇹🇼 繁體中文 (Traditional Chinese)  
- 🇨🇳 简体中文 (Simplified Chinese)  
- 🇹🇭 ไทย (Thai)  
- 🇻🇳 Tiếng Việt (Vietnamese)
- 🇫🇷 Français (French)  
- 🇩🇪 Deutsch (German)  
- 🇧🇷 Português (Brasil)
- 🇵🇱 Polski (Polish)
## TO DO
* Cache color_distance() results for faster read times on values (each computation is 0.02s~ atm)

## Development

1. Create a venv and install the requirements:
```
bash
py -m venv venv
source venv/bin/activate # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Install tesserocr on venv by downloading the wheel file accordingly:
```
https://github.com/simonflueckiger/tesserocr-windows_build/releases
https://pypi.org/project/tesserocr/

> pip install <package_name>.whl

```

3. run main.py to launch UI.
```
py main.py
```

## Special Thanks to Our Translators!

Thank you to the following individuals for contributing their time and effort to make this project accessible in multiple languages:

- 🇰🇷 **한국어 (Korean)**: Mono - @monoxerses  
- 🇹🇼 **繁體中文 (Traditional Chinese)**: JackyKuo (my goat)  
- 🇨🇳 **简体中文 (Simplified Chinese)**: JackyKuo
- 🇹🇭 **ไทย (Thai)**: Bushy - @bushy2018  
- 🇻🇳 **Tiếng Việt (Vietnamese)**: Kazucon - @pathetic384
- 🇫🇷 **Français (French)**: Luz - @luzushi  
- 🇩🇪 **Deutsch (German)**: Maddy - @madeleineaddyson
- 🇧🇷 **Português (Brasil)**: JJ - @jjftw1310
- 🇵🇱 **Polski (Polish)**: rogue - @onesloweredeyes


