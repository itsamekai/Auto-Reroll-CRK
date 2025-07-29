import tkinter as tk
from tkinter import ttk

ROLL_TYPES = [
    'AmplifyBuff', 'DMGResistBypass', 'DMGResist', 'CRIT%', 'ATK',
    'HP', 'DEF', 'ATKSPD', 'Cooldown', 'DebuffResist', 'DarkDMG',
    'IceDMG', 'SteelDMG', 'PoisonDMG', 'LightDMG', 'ElecDMG', 'FireDMG',
    'EarthDMG'
]

LINE_COUNTS = ['2', '3', '4']

def create_widgets(app, on_start_callback):
    tk.Label(app, text="Roll Type:").grid(row=0, column=0, padx=10, pady=5)
    roll_var = tk.StringVar(value=ROLL_TYPES[0])
    ttk.Combobox(app, textvariable=roll_var, values=ROLL_TYPES, state="readonly").grid(row=0, column=1)

    tk.Label(app, text="How many rolls?").grid(row=1, column=0, padx=10, pady=5)
    line_var = tk.StringVar(value=LINE_COUNTS[0])
    ttk.Combobox(app, textvariable=line_var, values=LINE_COUNTS, state="readonly").grid(row=1, column=1)

    tk.Label(app, text="Tainted Biscuit?").grid(row=2, column=0, padx=10, pady=5)
    tainted_var = tk.StringVar(value="Disabled")
    ttk.Combobox(app, textvariable=tainted_var, values=["Enabled", "Disabled"], state="readonly").grid(row=2, column=1)

    start_btn = tk.Button(app, text="Start", command=on_start_callback)
    start_btn.grid(row=3, column=0, columnspan=2, pady=10)

    tk.Label(app, text="Log Output:").grid(row=4, column=0, columnspan=2)
    log_box = tk.Text(app, height=12, width=75, state='disabled', wrap='word')
    log_box.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    scrollbar = tk.Scrollbar(app, command=log_box.yview)
    log_box.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=5, column=2, sticky='ns')

    return {
        "roll_var": roll_var,
        "line_var": line_var,
        "tainted_var": tainted_var,
        "log_box": log_box,
        "start_button": start_btn
}
