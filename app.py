import streamlit as st
from translate import translate_text
from languages import LANGUAGES
from speech import speech_to_text, load_model
from streamlit_mic_recorder import mic_recorder
from utils import get_english_pronunciation

st.set_page_config(page_title="AI Translator", page_icon="🌍")

st.title("🌍 AI Voice Translator")

# Load Whisper model (cached)
@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# Input text
text = st.text_input("Enter your text")

# Language dropdown
lang_name = st.selectbox("Select target language", list(LANGUAGES.keys()))
dest_lang = LANGUAGES[lang_name]

# 🎤 Voice Input
audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹ Stop Recording"
)

if audio:
    st.audio(audio["bytes"])

    spoken_text = speech_to_text(audio["bytes"], model)

    if spoken_text:
        st.success(f"You said: {spoken_text}")
        text = spoken_text   # overwrite text input
    else:
        st.error("Could not understand audio")

# 🔄 Translate Button
if st.button("Translate"):
    if text:
        output = translate_text(text, dest_lang)

        st.success("Translation done!")
        st.write(f"Translated Text: {output}")

        # 🔥 Add pronunciation
        pronunciation = get_english_pronunciation(output, dest_lang)
        st.info(f"English Pronunciation: {pronunciation}")

    else:
        st.warning("Please enter text")