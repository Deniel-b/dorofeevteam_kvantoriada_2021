import cv2
import numpy as np


LOGIN = "kekw"
PASS = "2204"
IP = "192.168.1.56"
PORT = "8080"


cap = cv2.VideoCapture("http://{}:{}@{}:{}/video".format(LOGIN, PASS, IP, PORT))









while True:


    window_name = "main"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1280, 720)
    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv2.imshow(window_name, frame)

    scale_percent = 60  # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    #print('Running..')





    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()