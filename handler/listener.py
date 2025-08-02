import keyboard
import threading
from handler.state import get_translator 

def start_esc_listener(is_running, set_running, log):
    def listen():
        while True:
            keyboard.wait("esc")
            if is_running():
                set_running(False)
                translator = get_translator()
                log(translator.text("esc_pressed"))

    threading.Thread(target=listen, daemon=True).start()    