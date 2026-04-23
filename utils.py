from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def get_english_pronunciation(text, lang_code):
    try:
        lang_map = {
            "hi": sanscript.DEVANAGARI,
            "ta": sanscript.TAMIL,
            "te": sanscript.TELUGU,
            "kn": sanscript.KANNADA,
            "ml": sanscript.MALAYALAM
        }

        if lang_code in lang_map:
            return transliterate(text, lang_map[lang_code], sanscript.ITRANS)
        else:
            return "Pronunciation not available"

    except Exception:
        return "Error in pronunciation"