import streamlit as st
import cv2
import tempfile

st.title("AI Football Scouting App")

uploaded_file = st.file_uploader("Upload a Player Video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())
    video = cv2.VideoCapture(temp_file.name)

    st.video(temp_file.name)

    # Example of reading video frame by frame
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        # Show frame (this will be updated with player detection later)
        st.image(frame, channels="BGR")
    video.release()
