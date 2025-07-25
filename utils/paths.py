import os
import sys

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_tesseract_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'Tesseract-OCR', 'tesseract.exe')
    else:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Tesseract-OCR', 'tesseract.exe'))


def get_writable_image_dir():

    if getattr(sys, 'frozen', False):
        # if bundled in app
        return os.path.expanduser("~/.reroll_images")
    else:
        # for dev env
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        images_dir = os.path.join(project_root, "images")
        return images_dir
    
WRITABLE_IMAGE_DIR = get_writable_image_dir()
os.makedirs(WRITABLE_IMAGE_DIR, exist_ok=True)   