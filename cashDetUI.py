import cv2 #Need to 'pip install opencv-python' to use cv2, for video output

cap = cv2.VideoCapture(0) #initializes video capture, '0' chooses default camera

while(True):
    ret, frame = cap.read()
    if(ret):
    
        frame = cv2.resize(frame,(640, 480)) #resize frame

        cv2.imshow('Cash Bill Detection Application',frame) #Displays frame with label

        if cv2.waitKey(1) & 0xFF ==ord('e'): #press 'e' to exit program application
            break

print('Still working :)') #print confirmation that the code exited properly, remove this before final submission
cap.release() #makes sure camera does not stay on after exiting code
cv2.destroyAllWindows() #makes sure all cv2 related systems are stopped