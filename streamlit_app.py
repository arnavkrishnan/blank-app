import streamlit as st
from utils import detect_image
from PIL import Image

# Streamlit app
st.title('Object Detection')

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    # Set detection thresholds
    obj_thresh = st.slider("Object Detection Threshold", 0.0, 1.0, 0.4)
    nms_thresh = st.slider("Non-Maximum Suppression Threshold", 0.0, 1.0, 0.45)

    detected_image = detect_image(image, obj_thresh=obj_thresh, nms_thresh=nms_thresh)

    st.image(detected_image, caption='Detected Image.', use_column_width=True)