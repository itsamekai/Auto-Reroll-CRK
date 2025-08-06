import tkinter as tk
from tkinter import ttk
from gui.app import create_widgets
from gui.event import on_start, start_listener
from utils.paths import set_tesseract_path
# set tesserocr
set_tesseract_path()
from utils.tesseract import api as tesseractAPI
from handler.state import setTranslateWidget, set_translator_language

def main():
    app = tk.Tk()
    app.title("Auto Reroll by Kai")
    app.option_add("*Font", "{Segoe UI} 11")

    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[10, 5])
    # tabs for setting / main page
    notebook = ttk.Notebook(app)
    notebook.pack(padx=10, pady=10, expand=True, fill='both')

    mainTab = ttk.Frame(notebook, padding=10)
    notebook.add(mainTab, text="Reroll")
    
    settingsTab = ttk.Frame(notebook, padding=10)
    notebook.add(settingsTab, text="Settings")

    instructionsTab = ttk.Frame(notebook, padding=10)
    notebook.add(instructionsTab, text="Instructions")

    # use indexes to determine the tabs accordingly
    setTranslateWidget("reroll_string", (notebook, 0))
    setTranslateWidget("settings_string", (notebook, 1))
    setTranslateWidget("instructions_string", (notebook, 2))

    # for logging to logbox in UI
    def log(msg):
        log_box.config(state='normal')
        log_box.insert(tk.END, msg + "\n")
        log_box.see(tk.END)
        log_box.config(state='disabled')

    # pass the variables & log fn
    def start_callback():
        on_start(widgets["roll_var"], widgets["line_var"], widgets["orange_var"], widgets["tainted_var"], widgets["chopsticks_var"], widgets["delay_var"], log, tesseractAPI)

    widgets = create_widgets(mainTab, settingsTab, instructionsTab, start_callback)
    log_box = widgets["log_box"]
    # start esc listener
    set_translator_language()
    start_listener(log)

    app.mainloop()

if __name__ == "__main__":
    main()
