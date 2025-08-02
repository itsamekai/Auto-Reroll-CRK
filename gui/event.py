import threading
from handler.listener import start_esc_listener
from handler.logic import run_task
from handler.state import is_running, set_running, set_translator_language, get_translator
from locale.translate import Translator



def on_start(roll_var, line_var, orange_var, tainted_var, delay_var, log, tesseractAPI):
    set_translator_language()
    translator = get_translator()

    if is_running():
        log("Task already running.")
        return

    # roll type returns in a tuple, i.e. 'ATK', tkinter.Booleanvar. check the 2nd.
    roll_type = [r for r, v in roll_var.items() if v.get()] # default EN name rolls
    if not roll_type:
        log(translator.text("non_selected"))
        return
    line_count = line_var.get()
    orange_bool = orange_var.get() == translator.text("rolls_enabled")
    tainted_bool = tainted_var.get() == translator.text("rolls_enabled")
    print(orange_bool, tainted_bool)
    delay = delay_var.get()
    
    if tainted_bool and int(line_count) > 3:
        log(translator.text("tainted_error"))
        return

    set_running(True)

    # Start ESC listener thread (only once, or ensure it starts once)
    # If you want to start it here, you can check a flag in core.app_state or start it at app init instead

    threading.Thread(
        target=run_task,
        args=(roll_type, line_count, orange_bool, tainted_bool, delay, tesseractAPI, log),
        daemon=True
    ).start()


def run_wrapper(roll_type, line_count, orange_bool, tainted_bool, delay, tesseractAPI, log_fn):
    try:
        run_task(roll_type, line_count, orange_bool, tainted_bool, delay, tesseractAPI, log_fn)
    finally:
        set_running(False)


# call once on start up
def start_listener(log_fn):
    start_esc_listener(is_running, set_running, log_fn)