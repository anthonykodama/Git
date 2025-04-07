import cv2 #Need to 'pip install opencv-python' to use cv2, for video output
from ultralytics import YOLO #Used for live object detection
import pyttsx3 #Text to speech library, need to 'pip install pyttsx3' to be used

best_model = 'best.pt' #brings best.pt model into program
cash_model = YOLO(best_model, task='detect') #loads the YOLO model
cash_labels = cash_model.names #gets cash labels ex. '1-front', '5-back'

cap = cv2.VideoCapture(0) #initializes video capture, '0' chooses default camera

def speak(command):
    engine = pyttsx3.init() #initializes text to speech for text output
    engine.say(command) #the text to speech will say whatever the 'command' string is assigned
    engine.runAndWait() #runs the 'speak' function

while(True):
    ret, frame = cap.read()
    if(ret):
    
        frame = cv2.resize(frame,(640, 480)) #resize frame

        results = cash_model(frame, verbose=False) #runs object detection on live frames, verbose=False eliminates live text output in console
        live_results = results[0].boxes #pulls the detected object's info
    
    if len(live_results) > 0: #if a cash object is detected the following code will proceed

        first_detection = live_results[0] #selects the first detection from the array of detections from live_results

        class_id = first_detection.cls.item() #assigns class ID from identified object and converts to int value
        class_name = cash_labels[class_id] #assigns cash label from the identified class ID

        conf_score = first_detection.conf.item() #gets confidence score and converts to float value

        if (conf_score) > 0.8: #Only provides text/speech output when confidence score is greater than 0.8
            cv2.putText(frame, f'{class_name} {conf_score}', (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2) #Bill label output
            speak(class_name) #runs 'speak' function with 'class_name' as the input

    cv2.imshow('Cash Bill Detection Application',frame) #Displays frame with label

    if cv2.waitKey(1) & 0xFF ==ord('e'): #press 'e' to exit program application
        break

print('Still working :)') #print confirmation that the code exited properly, remove this before final submission
cap.release() #makes sure camera does not stay on after exiting code
cv2.destroyAllWindows() #makes sure all cv2 related systems are stopped