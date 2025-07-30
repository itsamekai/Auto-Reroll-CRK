import tkinter as tk
from tkinter import ttk

ROLL_TYPES = [
    'AmplifyBuff', 'DMGResistBypass', 'DMGResist', 'CRIT%', 'ATK',
    'HP', 'DEF', 'ATKSPD', 'Cooldown', 'DebuffResist', 'DarkDMG',
    'IceDMG', 'SteelDMG', 'PoisonDMG', 'LightDMG', 'ElecDMG', 'FireDMG',
    'EarthDMG'
]

LINE_COUNTS = [2, 3, 4]

delay = [0, 0.1, 0.2, 0.3, 0.4, 0.5]

# probably not a clean solution
# added so I can just move the elements around in the array to reorder the UI
widgets = ["RollType", "RollCount", "Tainted", "Delay", "start", "log", "credit_name", "credit_server"]


def create_widgets(app, on_start_callback):
    tk.Label(app, text="Roll Type:").grid(row=widgets.index("RollType"), column=0, padx=10, pady=5)
    roll_var = tk.StringVar(value=ROLL_TYPES[0])
    ttk.Combobox(app, textvariable=roll_var, values=ROLL_TYPES, state="readonly").grid(row=widgets.index("RollType"), column=1)

    tk.Label(app, text="How many rolls?").grid(row=widgets.index("RollCount"), column=0, padx=10, pady=5)
    line_var = tk.StringVar(value=LINE_COUNTS[0])
    ttk.Combobox(app, textvariable=line_var, values=LINE_COUNTS, state="readonly").grid(row=widgets.index("RollCount"), column=1)

    tk.Label(app, text="Tainted Biscuit?").grid(row=widgets.index("Tainted"), column=0, padx=10, pady=5)
    tainted_var = tk.StringVar(value="Disabled")
    ttk.Combobox(app, textvariable=tainted_var, values=["Enabled", "Disabled"], state="readonly").grid(row=widgets.index("Tainted"), column=1)

    tk.Label(app, text="Add Delay").grid(row=widgets.index("Delay"), column=0, padx=10, pady=5)
    delay_var = tk.StringVar(value=delay[0])
    ttk.Combobox(app, textvariable=delay_var, values=delay, state="readonly").grid(row=widgets.index("Delay"), column=1)    

    start_btn = tk.Button(app, text="Start", command=on_start_callback)
    start_btn.grid(row=widgets.index("start"), column=0, columnspan=2, pady=10)

    tk.Label(app, text="Log Output:").grid(row=widgets.index("log"), column=0, columnspan=2)
    log_box = tk.Text(app, height=12, width=75, state='disabled', wrap='word')
    log_box.grid(row=widgets.index("log"), column=0, columnspan=2, padx=10, pady=5)

    scrollbar = tk.Scrollbar(app, command=log_box.yview)
    log_box.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=widgets.index("log"), column=2, sticky='ns')

    tk.Label(app, text="done by: Kai | discord: @boonkai", font=("Arial", 11)).grid(row=widgets.index("credit_name"), column=0, columnspan=2, sticky='w', padx=10)
    tk.Label(app, text="discord: discord.gg/creamery", font=("Arial", 11)).grid(row=widgets.index("credit_server"), column=0, sticky='w', padx=10)

    return {
        "roll_var": roll_var,
        "line_var": line_var,
        "tainted_var": tainted_var,
        "delay_var": delay_var,
        "log_box": log_box,
        "start_button": start_btn
}
