import os
import sys

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def set_tesseract_path():
    tesseract_dir = resource_path("TesseractLib")

    # Set TESSDATA_PREFIX for tesserocr
    tessdata_dir = os.path.join(tesseract_dir, "tessdata")
    os.environ['TESSDATA_PREFIX'] = tessdata_dir

    # add DLL directory explicitly for windows
    if sys.platform == "win32" and hasattr(os, "add_dll_directory"):
        os.add_dll_directory(tesseract_dir)
    else:
        # Fallback: prepend tesseract_dir to PATH
        os.environ['PATH'] = tesseract_dir + os.pathsep + os.environ.get('PATH', '')


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