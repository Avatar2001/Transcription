import streamlit as st
import whisper
import tempfile
import os

# Load Whisper model
model = whisper.load_model("base")

st.title("🎙️ Audio & Video Transcription App")
st.write("Upload an audio or video file, and I'll transcribe it for you.")

# File uploader
uploaded_file = st.file_uploader(
    "Upload an audio or video file",
    type=["mp3", "wav", "m4a", "mp4", "mkv", "mov"]
)

if uploaded_file is not None:
    # Save uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    # Preview media
    if uploaded_file.type.startswith("video/"):
        st.video(uploaded_file)
    else:
        st.audio(uploaded_file)

    # Transcribe button
    if st.button("Transcribe"):
        with st.spinner("Transcribing..."):
            result = model.transcribe(tmp_file_path)
            st.subheader("📜 Transcript")
            st.write(result["text"])

        # Clean up temp file
        os.remove(tmp_file_path)
