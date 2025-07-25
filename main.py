from utils.rarity import *
from utils.rolls import *
from utils.screenshot import *
from utils.click import *
import tkinter as tk
from tkinter import ttk
import threading
import time
import keyboard
import pytesseract
import os, sys


ROLL_TYPES = [
    'AmplifyBuff', 'DMGResistBypass', 'DMGResist', 'CRIT%', 'ATK',
    'HP', 'DEF', 'ATKSPD', 'Cooldown', 'DebuffResist', 'DarkDMG',
    'IceDMG', 'SteelDMG', 'PoisonDMG', 'LightDMG', 'ElecDMG', 'FireDMG',
    'EarthDMG'
]

LINE_COUNTS = ['2', '3', '4']

running = False

def log(msg):
    log_box.config(state='normal')
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)
    log_box.config(state='disabled')

def task_loop(roll_type, line_count):
    global running
    counter = 1  
    log("Starting auto reroll.")
    

    # init crk window from gpg
    crkWin = findAndResize('CookieRun') 
    while running:
        start = time.time()
        if not crkWin:
            log("CRK window not found. Open GPG.")
            break
        else:
            moveAndClick(crkWin) # start click
            time.sleep(1.14)
            screenshotValues(crkWin)
            cropValueBoxes()
            high_count, pos = getHighRarityCount()
            
            # check if the amount of purple / orange rolls is >= the no. of lines picked
            if (high_count >= int(line_count)):
                screenshotRoll(crkWin)
                rollResult, rolled = cropEnhanceRead(pos, roll_type, line_count)
                if rollResult:
                    elapsed = round(time.time() - start, 2)
                    log(f"Successfully rolled. Total: {counter} rolls done. {elapsed} time taken.")
                    break
                else:
                    elapsed = round(time.time() - start, 2)
                    log(f"Roll {counter}: {high_count} high values but wrong rolls - {rolled}. {elapsed} time taken.")
                    counter+= 1
            else:
                elapsed = round(time.time() - start, 2)
                log(f"Roll {counter}: {high_count} high values. {elapsed}s time taken.")
                counter+= 1
            

    log("auto reroll stopped.")

def on_start():
    global running
    if running:
        log("Already running.")
        return

    roll_type = roll_type_var.get()
    line_count = line_count_var.get() 
    running = True
    threading.Thread(target=task_loop, args=(roll_type, line_count), daemon=True).start()

def listen_for_esc():
    global running
    while True:
        keyboard.wait("esc")
        if running:
            running = False
            log("ESC pressed — stopping task.")


app = tk.Tk()
app.title("Auto Reroll")

# dropdown for roll selector & no. of lines
tk.Label(app, text="Roll Type:").grid(row=0, column=0, padx=10, pady=5)
roll_type_var = tk.StringVar()
roll_dropdown = ttk.Combobox(app, textvariable=roll_type_var, values=ROLL_TYPES, state="readonly")
roll_dropdown.grid(row=0, column=1, padx=10, pady=5)
roll_dropdown.set(ROLL_TYPES[0])

tk.Label(app, text="How many rolls?").grid(row=1, column=0, padx=10, pady=5)
line_count_var = tk.StringVar()
line_dropdown = ttk.Combobox(app, textvariable=line_count_var, values=LINE_COUNTS, state="readonly")
line_dropdown.grid(row=1, column=1, padx=10, pady=5)
line_dropdown.set(LINE_COUNTS[0])

# start button
submit_btn = tk.Button(app, text="Start", command=on_start)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10)

# log box
tk.Label(app, text="Log Output:").grid(row=3, column=0, columnspan=2)
log_box = tk.Text(app, height=12, width=75, state='disabled', wrap='word')
log_box.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

scrollbar = tk.Scrollbar(app, command=log_box.yview)
log_box.config(yscrollcommand=scrollbar.set)
scrollbar.grid(row=4, column=2, sticky='ns')

# keyboard listener to exit
threading.Thread(target=listen_for_esc, daemon=True).start()

app.mainloop()

