import atexit
try:
    from tesserocr import PyTessBaseAPI
except ImportError as e:
    PyTessBaseAPI = None
    print("tessocr not imported properly.")

from utils.paths import resource_path



api = None

# exit tesserocr safely 
def cleanup_tesseract():
    try:
        api.End()
    except Exception:
        pass


if PyTessBaseAPI:
    try:
        api = PyTessBaseAPI(resource_path("TesseractLib/tessdata"))
        api.SetVariable("tessedit_char_whitelist", "%ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        atexit.register(cleanup_tesseract)
    except Exception as e:
        print("Error on init tesseract api.")
        api = None