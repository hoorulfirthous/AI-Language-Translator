import streamlit as st
from translate import translate_text
from languages import LANGUAGES

st.set_page_config(page_title="AI Translator", page_icon="🌍")

st.title("🌍 AI Translator")

#input
text = st.text_input("Enter your text")

#language list
lang_name = st.selectbox("Select target language", list(LANGUAGES.keys()))
dest_lang = LANGUAGES[lang_name]

if st.button("Translate"):
    if text and dest_lang:
        output = translate_text(text, dest_lang)
        st.success("Translation done!")
        st.write(output)
    else:
        st.warning("Please enter both text and language")