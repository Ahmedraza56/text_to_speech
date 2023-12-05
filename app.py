import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text)
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

# Function to set download link for audio file
def get_audio_download_link(buffer, filename="audio.mp3"):
    buffer.seek(0)
    b64_data = base64.b64encode(buffer.read()).decode()
    href = f'<a href="data:audio/mp3;base64,{b64_data}" download="{filename}">Download audio file</a>'
    return href

# Create Streamlit application
st.title('Text to Speech Converter')

# Input for text from user
user_input_text = st.text_area("Enter the text you want to convert to speech:")

if st.button('Convert'):
    if user_input_text:
        # Call function to convert text to speech
        audio_buffer = text_to_speech(user_input_text)

        # Display audio player and download link
        st.audio(audio_buffer, format="audio/mp3", start_time=0)
        st.markdown(get_audio_download_link(audio_buffer), unsafe_allow_html=True)
    else:
        st.warning('Please input some text to convert.')



