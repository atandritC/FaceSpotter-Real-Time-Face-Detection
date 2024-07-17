import streamlit as st
from main import detect_faces
from PIL import Image

st.title("FaceSpotter")
st.text("Real-Time Face Detection using OpenCV and dlib")

frame_placeholder = st.empty()

if 'is_running' not in st.session_state:
    st.session_state.is_running = False

def toggle_detection():
    st.session_state.is_running = not st.session_state.is_running

if st.session_state.is_running:
    button_text = 'Stop Face Detection'
    button_color = 'red'
else:
    button_text = 'Start Face Detection'
    button_color = 'green'

st.markdown(f"""
    <style>
    .stButton > button {{
        background-color: {button_color};
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

if st.button(button_text, on_click=toggle_detection):
    pass

if st.session_state.is_running:
    for frame in detect_faces():
        img = Image.fromarray(frame)
        frame_placeholder.image(img, use_column_width=True)
        
        if not st.session_state.is_running:
            break