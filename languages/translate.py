import json
import os
import sys

class Translator:
    def __init__(self, lang='en', locale_path=None):
        if locale_path is None:
            if getattr(sys, 'frozen', False): # if on app
                base_path = os.path.join(sys._MEIPASS, 'languages')
            else:
                base_path = os.path.dirname(os.path.abspath(__file__))
                
            locale_path = os.path.join(base_path, 'translations')
        
        self.lang = lang
        self.locale_path = locale_path
        self.translations = self.load_translations()

    def load_translations(self):
        file_path = os.path.join(self.locale_path, f"{self.lang}.json")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:   
            return {}
        
    def set_language(self, lang_code):
        self.lang = lang_code
        self.translations = self.load_translations()

    def text(self, key, **kwargs):
        return self.translations.get(key, key).format(**kwargs)
    
        # translate rolls to localized language before logging
    def translate_rolls(self, keys: list[str]) -> list[str]:
        return [self.translations.get(key, key) for key in keys]

