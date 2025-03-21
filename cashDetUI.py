import cv2 #Need to 'pip install opencv-python' to use cv2, for video output
from ultralytics import YOLO #Used for live object detection

best_model = 'best.pt' #brings best.pt model into program
cash_model = YOLO(best_model, task='detect') #loads the YOLO model
cash_labels = cash_model.names #gets cash labels ex. '1-front', '5-back'

cap = cv2.VideoCapture(0) #initializes video capture, '0' chooses default camera

while(True):
    ret, frame = cap.read()
    if(ret):
    
        frame = cv2.resize(frame,(640, 480)) #resize frame

        results = cash_model(frame, verbose=False) #runs object detection on live frames, verbose=False eliminates live text output in console

        cv2.putText(frame, 'Bill Label Output', (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2) #Bill label output

        cv2.imshow('Cash Bill Detection Application',frame) #Displays frame with label

        if cv2.waitKey(1) & 0xFF ==ord('e'): #press 'e' to exit program application
            break

print('Still working :)') #print confirmation that the code exited properly, remove this before final submission
cap.release() #makes sure camera does not stay on after exiting code
cv2.destroyAllWindows() #makes sure all cv2 related systems are stopped