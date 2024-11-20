import streamlit as st
from bark import SAMPLE_RATE, generate_audio, preload_models

preload_models()

st.title("Bark AI Example 🔊")

prompt = st.chat_input("Say something")

if prompt:
    audio_array = generate_audio(prompt)
    st.audio(audio_array,format="audio/mpeg",sample_rate=SAMPLE_RATE)