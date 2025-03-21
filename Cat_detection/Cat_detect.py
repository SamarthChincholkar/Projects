import streamlit as st # type: ignore
import cv2
import numpy as np
import torch
from ultralytics import YOLO
from PIL import Image

# Load YOLOv8 model (ensure best.pt is in the same folder)
model = YOLO("best.pt")

# Streamlit UI
st.title("🐱 Real-Time Cat Detection")
st.sidebar.header("Settings")
conf_threshold = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.5)
mode = st.sidebar.radio("Choose Mode", ["Upload Image", "Live Camera"])

# Function to perform detection
def detect_objects(image):
    results = model(image, conf=conf_threshold)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            label = f"Cat {conf:.2f}"
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

if mode == "Upload Image":
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        detected_image = detect_objects(image)
        st.image(cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB), caption="Detected Cats", use_column_width=True)

elif mode == "Live Camera":
    st.write("### 📡 Connect Your iPhone Camera")
    st.info("Use an IP Camera App (e.g., IP Webcam) and enter the stream URL below:")
    ip_url = st.text_input("Enter RTSP/MJPEG URL", "http://your-iphone-ip:8080/video")
    
    if st.button("Start Detection"):
        cap = cv2.VideoCapture(ip_url)
        stframe = st.empty()
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to capture video. Check the IP Camera URL.")
                break
            frame = detect_objects(frame)
            stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")
        cap.release()
