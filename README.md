# Steps to Use
1) Turn on CRK with GPG.
2) Go to beascuit reroll page. 
3) Make sure all warning pop ups are gone. (>= 2 rolls, initial roll warnings)
4) Select lines needed (>= lines) & roll type. 

## TO DO
* refactor UI out of main for better clarity
* Read Numbers (not that important, but nice to have?) 
* Improve runtime per roll - needs more optimisation atm
    * current reads at 1.3s~
    * current ocr read at 2.2s~
* Add more emulator support. 
* ~~Add support for tainted biscuits.~~
* ~~Add support for other elemental rolls.~~
* ~~Check positional values to ensure that n number of rolls matches the roll we _actually_ want.~~ 

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