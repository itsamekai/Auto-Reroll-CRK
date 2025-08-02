import tkinter as tk
from tkinter import ttk
from locale.translate import Translator
from handler.state import *

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
widgets = ["Language", "RollType", "RollCount", "OrangeOnly", "Tainted", "Delay", "start", "log", "credit_name", "credit_server"]

# dynamically change languages
translator = get_translator()

def changeLanguage(lang):
    lang_code = AVAILABLE_LANGUAGES.get(lang, "en")
    set_lang(lang_code)
    set_translator_language()
    for k, widget in getTranslateWidget().items():
        if isinstance(widget, (tk.Label, ttk.Button)):
            widget.config(text=translator.text(k))
            
        # since we only got comboboxes with disable / enable.
        elif isinstance(widget, ttk.Combobox):
            widget.config(values=[
                translator.text("rolls_enabled"),
                translator.text("rolls_disabled")
            ])
        
        # changes the default enable / disable values 
        elif isinstance(widget, tk.StringVar): 
            widget.set(translator.text("rolls_disabled"))

        # changes the tab names
        elif isinstance(widget, tuple):
            notebook, tab_index = widget
            notebook.tab(tab_index, text=translator.text(k))


# widgets for 'Reroll' tab
def createRerollWidgets(mainTab, on_start_callback):

    lang_var = tk.StringVar(value=list(AVAILABLE_LANGUAGES.keys())[0])
    lang_menu = ttk.Combobox(mainTab, textvariable=lang_var, values=list(AVAILABLE_LANGUAGES.keys()), state="readonly")
    lang_menu.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    lang_menu.bind("<<ComboboxSelected>>", lambda event: changeLanguage(lang_var.get()))  

    start_btn = tk.Button(mainTab, text=translator.text("start_button"), command=on_start_callback)
    start_btn.grid(row=1, column=0, columnspan=2, pady=10)


    tk.Label(mainTab, text="Log Output:").grid(row=widgets.index("log"), column=0, columnspan=2)
    log_box = tk.Text(mainTab, height=12, width=70, state='disabled', wrap='word')
    log_box.grid(row=widgets.index("log"), column=0, columnspan=2, padx=10, pady=5)
    log_box.config(font=("TkDefaultFont", 12))

    scrollbar = tk.Scrollbar(mainTab, command=log_box.yview)
    log_box.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=widgets.index("log"), column=2, sticky='ns')

    creditName = tk.Label(mainTab, text=translator.text("credit_name"), font=("Arial", 11))
    creditName.grid(row=widgets.index("credit_name"), column=0, columnspan=2, sticky='w', padx=10)

    creditServer = tk.Label(mainTab, text=translator.text("credit_server"), font=("Arial", 11))
    creditServer.grid(row=widgets.index("credit_server"), column=0, sticky='w', padx=10)
   
    setTranslateWidget("start", start_btn)
    setTranslateWidget("credit_name", creditName)
    setTranslateWidget("credit_server", creditServer)

    return log_box, start_btn

# combine a dropdown and a toggle checkbox to select multiple
def createSelectRollType(parent, row):

    roll_type_label = tk.Label(parent, text=translator.text("settings_roll_type"))
    roll_type_label.grid(row=row, column=0, padx=10, pady=5)
    setTranslateWidget("settings_roll_type", roll_type_label)

    roll_vars = {roll: tk.BooleanVar(value=False) for roll in ROLL_TYPES}

    def toggle_dropdown():
        if hasattr(toggle_dropdown, "popup") and toggle_dropdown.popup.winfo_exists():
            toggle_dropdown.popup.destroy()
            return

        # pop up window for selecting
        toggle_dropdown.popup = tk.Toplevel(parent)
        toggle_dropdown.popup.wm_overrideredirect(True) # acts as a window, set true 
        toggle_dropdown.popup.attributes("-topmost", True)

        # Position near the button
        x = dropdown_btn.winfo_rootx()
        y = dropdown_btn.winfo_rooty() + dropdown_btn.winfo_height()
        toggle_dropdown.popup.geometry(f"+{x}+{y}")

        # add a border to popup 
        border_frame = tk.Frame(toggle_dropdown.popup, bg="#444", bd=1)
        border_frame.pack(padx=1, pady=1)
        content_frame = tk.Frame(border_frame, bg="white", padx=5, pady=5)
        content_frame.pack()

        # checkboxes in popup
        for roll in ROLL_TYPES:
            label = translator.text(roll)
            cb = tk.Checkbutton(content_frame, text=label, variable=roll_vars[roll], anchor="w", bg="white", relief="flat", font=("TkDefaultFont", 11))
            cb.pack(anchor="w", fill="x")

        # event listener for when clicking out
        def click_outside(event):
            def check():
                widget = event.widget
                while widget is not None:
                    if widget == toggle_dropdown.popup:
                        return
                    widget = widget.master
                if toggle_dropdown.popup.winfo_exists():
                    toggle_dropdown.popup.destroy()
                    parent.unbind_all("<Button-1>")
                
            toggle_dropdown.popup.after_idle(check)

        parent.bind_all("<Button-1>", click_outside, add="+")

    dropdown_btn = ttk.Button(parent, text=translator.text("dropdown_select_rolls"), command=toggle_dropdown)
    dropdown_btn.grid(row=row, column=1, padx=10, pady=5)

    setTranslateWidget("dropdown_select_rolls", dropdown_btn)

    return roll_vars

# widgets for 'Settings' tab   
def createSettingsWidgets(settingsTab):

    # RollCount - no. of rolls, 2 to 4. (tainted max 3.)
    roll_count = tk.Label(settingsTab, text=translator.text("settings_roll_count"))
    roll_count.grid(row=widgets.index("RollCount"), column=0, padx=10, pady=5)
    line_var = tk.StringVar(value=LINE_COUNTS[0])
    ttk.Combobox(settingsTab, textvariable=line_var, values=LINE_COUNTS, state="readonly").grid(row=widgets.index("RollCount"), column=1)

    # OrangeOnly - auto reroller only stops if n number of lines are orange.     
    orange_only = tk.Label(settingsTab, text=translator.text("settings_orange_only"))
    orange_only.grid(row=widgets.index("OrangeOnly"), column=0, padx=10, pady=5)
    orange_var = tk.StringVar(value=translator.text("rolls_disabled"))
    en_dis_orange = ttk.Combobox(settingsTab, textvariable=orange_var, values=[translator.text("rolls_enabled"), translator.text("rolls_disabled")], state="readonly")
    en_dis_orange.grid(row=widgets.index("OrangeOnly"), column=1)


    # Tainted - option for tainted beascuits. only 3 rolls.
    tainted_label = tk.Label(settingsTab, text=translator.text("settings_tainted_biscuit"))
    tainted_label.grid(row=widgets.index("Tainted"), column=0, padx=10, pady=5)
    tainted_var = tk.StringVar(value=translator.text("rolls_disabled"))
    en_dis_tainted = ttk.Combobox(settingsTab, textvariable=tainted_var, values=[translator.text("rolls_enabled"), translator.text("rolls_disabled")], state="readonly")
    en_dis_tainted.grid(row=widgets.index("Tainted"), column=1)
    
    

    
    # Delay - in case OCR has error reading, manually adding a delay can allow more time for the 'Bling' to settle.
    delay_choice = tk.Label(settingsTab, text=translator.text("settings_add_delay"))
    delay_choice.grid(row=widgets.index("Delay"), column=0, padx=10, pady=5)
    delay_var = tk.StringVar(value=delay[0])
    ttk.Combobox(settingsTab, textvariable=delay_var, values=delay, state="readonly").grid(row=widgets.index("Delay"), column=1)  
    
    # global widgets for translation update
    setTranslateWidget("settings_roll_count", roll_count)
    setTranslateWidget("settings_add_delay", delay_choice)
    setTranslateWidget("settings_orange_only", orange_only)
    setTranslateWidget("default_orange", orange_var)
    setTranslateWidget("default_tainted", tainted_var)
    setTranslateWidget("settings_tainted_biscuit", tainted_label)
    setTranslateWidget("en_dis_orange", en_dis_orange)
    setTranslateWidget("en_dis_tainted", en_dis_tainted)

    
    return line_var, orange_var, tainted_var, delay_var


# widgets for 'Instructions' tab
def createInstructionsWidgets(instructionsTab):
    for i in range(1, 6):
        key = f"instruction_{i}"
        label = tk.Label(instructionsTab, text=translator.text(key), anchor="w", justify="left")
        label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
        # translate_widgets[key] = label
        setTranslateWidget(key, label)

# init all widgets and return
def create_widgets(mainTab, settingsTab, instructionsTab, on_start_callback):
    roll_var = createSelectRollType(settingsTab, row=widgets.index("RollType")) 
    log_box, start_btn = createRerollWidgets(mainTab, on_start_callback)
    line_var, orange_var, tainted_var, delay_var = createSettingsWidgets(settingsTab)
    createInstructionsWidgets(instructionsTab)

    return {
        "roll_var": roll_var,
        "line_var": line_var,
        "orange_var": orange_var,
        "tainted_var": tainted_var,
        "delay_var": delay_var,
        "log_box": log_box,
        "start_button": start_btn
}
