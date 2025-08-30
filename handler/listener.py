from pynput import keyboard
import threading
from handler.state import get_translator 

def start_esc_listener(is_running, set_running, log):
    def on_press(key):
        if key == keyboard.Key.esc and is_running():
            set_running(False)
            translator = get_translator()
            log(translator.text("esc_pressed"))

    # Start the listener in a daemon thread
    listener = keyboard.Listener(on_press=on_press)
    listener.daemon = True
    listener.start()