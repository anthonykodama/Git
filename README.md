# **Cash Bill Detection Application for the Blind**
This project is the creation of a cash bill object detection system that is designed specifically for the blind/visually impaired population within the United States. 
There are two major portions to this project which consist of training an object detection model and implementing the trained object detection model into a desktop program.
## Cash Object Detection Model Implementation
### 1. Implementation Requirements
Anaconda (Virtual Environment)  
Visual Studio Code (Python 3.12)
### 2. Implementation Installation
ultralytics - Used for live object detection   
cv2 - Used for live webcam video output  
pyttsx3 - Used for Text to Speech  
Copy the code (cashDetUI.py) into vsCode python file  
Download the trained model (best.pt) and put it in the same folder as the code
### 3. Implementation Usage
#### In Anaconda Command Prompt:
Create Virtual Environment '''conda create --name cash_detect_env python=3.12'''  
ultralytics '''pip install ultralytics'''   
cv2 '''pip install opencv-python'''  
pyttsx3 '''pip install pyttsx3'''  
Run the code '''python cashDetUI.py'''  
Press 'e' to exit the application
