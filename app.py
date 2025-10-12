import streamlit as st
import speech_recognition as sr

st.title("🎤 Voice to Text Converter")

# Create two buttons side by side
col1, col2 = st.columns(2)

if col1.button("🎙️ Start Recording"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
        st.write("Recognizing...")
        try:
            text = r.recognize_google(audio)
            st.success(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError:
            st.error("Could not connect to the speech recognition service.")

if col2.button("⏹ Stop Recording"):
    st.info("Recording stopped manually.")
