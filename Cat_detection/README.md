 Cat Detection Project Using YOLOv8  

My Cat Detection project leverages Ultralytics YOLOv8, a state-of-the-art deep learning model, to identify and classify cats in real-time using computer vision. The goal was to create a highly accurate and efficient detection system that could process live input from a webcam or smartphone camera.  

 Project Workflow  
1. Data Collection & Preprocessing  
   - I gathered a diverse dataset of cat images, ensuring variations in breed, pose, lighting, and background.  
   - The dataset was annotated with bounding boxes to help YOLOv8 learn object localization.  

2. Model Training on Kaggle  
   - I fine-tuned the YOLOv8 model on my custom dataset using transfer learning.  
   - I optimized hyperparameters such as learning rate and batch size for better accuracy.  
   - The best-performing weights were saved locally for deployment.  

3. Building a Streamlit Web App  
   - I integrated Streamlit to create an interactive UI, enabling users to upload images or stream live video for detection.  
   - The app runs real-time inference using the trained YOLOv8 model and overlays bounding boxes around detected cats.  

4. iPhone Camera Integration  
   - To enhance usability, I configured iPhone’s camera as a live input source, allowing real-time detection with mobile accessibility.  

5. Objective and Motivation
   - My bike in my garage started getting all kinds of scratches on the tank and I could not figure out the reason until one night I saw a cat climb on top of the seat and sit on it. I figured it must sleep there every night or so.
   - Hence I decided to create an AI based surveillance that would help help me deal with this. Once cat detected, I can leverage arduino components such as speaker outputting dog bark sounds or any other method to cause the cat to leave my bike alone. 

 Outcome & Impact  
- Achieved high accuracy in detecting cats with minimal false positives.  
- Provided an interactive and user-friendly web-based interface.  
- Demonstrated efficient real-time processing, making it suitable for various applications, including pet monitoring and wildlife tracking.
