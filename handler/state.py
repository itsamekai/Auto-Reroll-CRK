_running = False

def is_running():
    global _running
    return _running

def set_running(value: bool):
    global _running
    _running = value