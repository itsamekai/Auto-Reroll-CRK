from languages.translate import Translator
_running = False
_lang = "en"
_translate_widgets = {}
_translator = Translator()

AVAILABLE_LANGUAGES = {
    "English": "en",
    "한국인": "kr",
    "繁體中文": "zh-TW", # Traditional Chinese
    "简体中文": "zh-CN",  # Simplified Chinese
    "ไทย": "th",
    "Tiếng Việt": "vi",
    "Français": "fr",
    "Deutsch" : "de",
    "Polski": "pl",
    "Português (Brasil)": "pt-BR"    
}

def is_running():
    global _running
    return _running

def set_running(value: bool):
    global _running
    _running = value

def get_lang():
    global _lang
    return _lang

def set_lang(new_lang):
    global _lang
    _lang = new_lang

def setTranslateWidget(key, value):
    global _translate_widgets
    _translate_widgets[key] = value

def getTranslateWidget():
    global _translate_widgets
    return _translate_widgets

def get_translator():
    return _translator

def set_translator_language():
    _translator.set_language(get_lang())

