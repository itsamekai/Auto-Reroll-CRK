import keyboard
import threading

def start_esc_listener(is_running, set_running, log):
    def listen():
        while True:
            keyboard.wait("esc")
            if is_running():
                set_running(False)
                log("ESC pressed — stopping task.")

    threading.Thread(target=listen, daemon=True).start()