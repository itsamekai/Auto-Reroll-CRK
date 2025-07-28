from utils.rarity import *
from utils.rolls import *
from utils.screenshot import *
from utils.click import *
import tkinter as tk
from tkinter import ttk
import threading
import time
import keyboard


ROLL_TYPES = [
    'AmplifyBuff', 'DMGResistBypass', 'DMGResist', 'CRIT%', 'ATK',
    'HP', 'DEF', 'ATKSPD', 'Cooldown', 'DebuffResist', 'DarkDMG',
    'IceDMG', 'SteelDMG', 'PoisonDMG', 'LightDMG', 'ElecDMG', 'FireDMG',
    'EarthDMG'
]

LINE_COUNTS = ['2', '3', '4']

CONST_RESET_BUTTON_PATH = resource_path("template/reset_button.png")

running = False


def log(msg):
    log_box.config(state='normal')
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)
    log_box.config(state='disabled')

def task_loop(roll_type, line_count, tainted_bool):
    global running  
    counter = 1  
    log("Starting auto reroll.")

    # init crk window from gpg
    crkWin = findAndResize('CookieRun')
    # get the reset button location coordinates
    crkImage = screenshotWindow(crkWin)
    resetLoc = findResetButton(CONST_RESET_BUTTON_PATH, crkImage)
    print(f"reset button location: {resetLoc}") 

    while running:
        start = time.time()
        if not crkWin:
            log("CRK window not found. Open GPG.")
            break
        else:
            if not isinstance(resetLoc, tuple):
                log("Reset button not found. Check UI.")
                break
            moveAndClick(crkWin, resetLoc) # start click
            time.sleep(1.1)
            value_screenshot = screenshotValues(crkWin)
            cropped = cropValueBoxes(value_screenshot, tainted_bool)
            high_count, pos = getHighRarityCount(cropped)
            
            # check if the amount of purple / orange rolls is >= the no. of lines picked
            if (high_count >= int(line_count)):
                roll_screenshot = screenshotRoll(crkWin)
                rollResult, rolled = cropEnhanceRead(pos, roll_type, line_count, roll_screenshot, tainted_bool)
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
    running = False

def on_start():
    global running
    if running:
        log("Already running.")
        return

    roll_type = roll_type_var.get()
    line_count = line_count_var.get()
    tainted_bool = tainted_bool_var.get() == "Enabled"

    if tainted_bool and int(line_count) >3:
        log("Tainted only allows a line count of below 4. Stopping.")
        return

    running = True
    threading.Thread(target=task_loop, args=(roll_type, line_count, tainted_bool), daemon=True).start()

def listen_for_esc():
    global running
    while True:
        keyboard.wait("esc")
        if running:
            running = False
            log("ESC pressed — stopping task.")


app = tk.Tk()
app.title("Auto Reroll by Kai")

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

tk.Label(app, text="Tainted Beascuit?").grid(row=2, column=0, padx=10, pady=5)
tainted_bool_var = tk.StringVar(value="Disabled")
tainted_dropdown = ttk.Combobox(app, textvariable=tainted_bool_var, values=["Enabled", "Disabled"], state="readonly")
tainted_dropdown.grid(row=2, column=1, padx=10, pady=5)
tainted_dropdown.set("Disabled")


# start button
submit_btn = tk.Button(app, text="Start", command=on_start)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# log box
tk.Label(app, text="Log Output:").grid(row=4, column=0, columnspan=2)
log_box = tk.Text(app, height=12, width=75, state='disabled', wrap='word')
log_box.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

scrollbar = tk.Scrollbar(app, command=log_box.yview)
log_box.config(yscrollcommand=scrollbar.set)
scrollbar.grid(row=5, column=2, sticky='ns')

tk.Label(app, text="done by: Kai | discord: @boonkai", font=("Arial", 11)).grid(row=6, column=0, columnspan=2, sticky='w', padx=10)
tk.Label(app, text="discord: discord.gg/creamery", font=("Arial", 11)).grid(row=7, column=0, sticky='w', padx=10)

# keyboard listener to exit
threading.Thread(target=listen_for_esc, daemon=True).start()

app.mainloop()

