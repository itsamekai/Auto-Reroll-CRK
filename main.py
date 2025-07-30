import tkinter as tk
from gui.app import create_widgets
from gui.event import on_start, start_listener
from utils.paths import set_tesseract_path
# set tesserocr
set_tesseract_path()
from utils.tesseract import api as tesseractAPI


def main():
    app = tk.Tk()
    app.title("Auto Reroll by Kai")

    # for logging to logbox in UI
    def log(msg):
        log_box.config(state='normal')
        log_box.insert(tk.END, msg + "\n")
        log_box.see(tk.END)
        log_box.config(state='disabled')

    # pass the variables & log fn
    def start_callback():
        on_start(widgets["roll_var"], widgets["line_var"], widgets["tainted_var"], widgets["delay_var"], log, tesseractAPI)

    widgets = create_widgets(app, start_callback)
    log_box = widgets["log_box"]
    # start esc listener
    start_listener(log)

    app.mainloop()

if __name__ == "__main__":
    main()
