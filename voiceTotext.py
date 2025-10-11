import streamlit as st
import speech_recognition as sr

st.title("🎤 Voice to Text Converter")

if st.button("Start Recording"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
        st.write("Recognizing...")
        try:
            text = r.recognize_google(audio)
            st.success(f"Recognized Text: {text}")
        except:
            st.error("Could not understand audio.")
