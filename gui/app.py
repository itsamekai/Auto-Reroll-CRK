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

instructions = [
    "1. Turn on CRK with Google Play Games. (Ensure CRK is in EN language)",
    "2. Go to beascuit roll page.",
    "3. Disable warning pop-ups on beascuit warnings.",
    "4. Modify settings accordingly in settings tab.",
    "5. Start button to start. ESC key to stop."
    ]

# probably not a clean solution
# added so I can just move the elements around in the array to reorder the UI
widgets = ["RollType", "RollCount", "Tainted", "Delay", "start", "log", "credit_name", "credit_server"]

# widgets for 'Reroll' tab
def createRerollWidgets(mainTab, on_start_callback):
    start_btn = tk.Button(mainTab, text="Start", command=on_start_callback)
    start_btn.grid(row=widgets.index("start"), column=0, columnspan=2, pady=10)

    tk.Label(mainTab, text="Log Output:").grid(row=widgets.index("log"), column=0, columnspan=2)
    log_box = tk.Text(mainTab, height=12, width=75, state='disabled', wrap='word')
    log_box.grid(row=widgets.index("log"), column=0, columnspan=2, padx=10, pady=5)

    scrollbar = tk.Scrollbar(mainTab, command=log_box.yview)
    log_box.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=widgets.index("log"), column=2, sticky='ns')

    tk.Label(mainTab, text="done by: Kai | discord: @boonkai", font=("Arial", 11)).grid(row=widgets.index("credit_name"), column=0, columnspan=2, sticky='w', padx=10)
    tk.Label(mainTab, text="discord: discord.gg/creamery", font=("Arial", 11)).grid(row=widgets.index("credit_server"), column=0, sticky='w', padx=10)

    return log_box, start_btn 


# widgets for 'Settings' tab   
def createSettingsWidgets(settingsTab):
    tk.Label(settingsTab, text="Roll Type:").grid(row=widgets.index("RollType"), column=0, padx=10, pady=5)
    roll_var = tk.StringVar(value=ROLL_TYPES[0])
    ttk.Combobox(settingsTab, textvariable=roll_var, values=ROLL_TYPES, state="readonly").grid(row=widgets.index("RollType"), column=1)

    tk.Label(settingsTab, text="How many rolls?").grid(row=widgets.index("RollCount"), column=0, padx=10, pady=5)
    line_var = tk.StringVar(value=LINE_COUNTS[0])
    ttk.Combobox(settingsTab, textvariable=line_var, values=LINE_COUNTS, state="readonly").grid(row=widgets.index("RollCount"), column=1)

    tk.Label(settingsTab, text="Tainted Biscuit?").grid(row=widgets.index("Tainted"), column=0, padx=10, pady=5)
    tainted_var = tk.StringVar(value="Disabled")
    ttk.Combobox(settingsTab, textvariable=tainted_var, values=["Enabled", "Disabled"], state="readonly").grid(row=widgets.index("Tainted"), column=1)

    tk.Label(settingsTab, text="Add Delay").grid(row=widgets.index("Delay"), column=0, padx=10, pady=5)
    delay_var = tk.StringVar(value=delay[0])
    ttk.Combobox(settingsTab, textvariable=delay_var, values=delay, state="readonly").grid(row=widgets.index("Delay"), column=1)  

    return roll_var, line_var, tainted_var, delay_var


# widgets for 'Instructions' tab
def createInstructionsWidgets(instructionsTab):
    for i, inst in enumerate(instructions):
        label = tk.Label(instructionsTab, text=inst, anchor="w", justify="left")
        label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

# init all widgets and return
def create_widgets(mainTab, settingsTab, instructionsTab, on_start_callback):
    log_box, start_btn = createRerollWidgets(mainTab, on_start_callback)
    roll_var, line_var, tainted_var, delay_var = createSettingsWidgets(settingsTab)
    createInstructionsWidgets(instructionsTab)

    return {
        "roll_var": roll_var,
        "line_var": line_var,
        "tainted_var": tainted_var,
        "delay_var": delay_var,
        "log_box": log_box,
        "start_button": start_btn
}
