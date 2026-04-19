from deep_translator import GoogleTranslator

def translate_text(text, dest_lang):
    translated = GoogleTranslator(target=dest_lang).translate(text)
    return translated