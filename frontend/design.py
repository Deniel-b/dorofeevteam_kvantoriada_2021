import eel
import cv2
import asyncio
import numpy as np
import time
voiceTrue = False

#for ip camera
#cam1
ip1 = "10.188.96.150"
port1 = "8000"
login1 = "admin"
password1 = "admin"
ip2 = "0.0.0.1"
port2 = "7777"
login2 = "Zeon"
password2 = "22882"

#cv
cap = 0
def cv(capture):
    global cap
    cap = cv2.VideoCapture("http://{}:{}/videofeed".format(ip1, port1))
    while True:
        try:
            window_name = "cam1"
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
                return 0
                break
        except:
            return 0
    cap.release()
    cv2.destroyAllWindows()
    
#eel
@eel.expose
def starterVoice(lolvoice):
    lolvoice += 1
    global voiceTrue
    if lolvoice == 2:
        lolvoice = 0
    if lolvoice == 0:
        voiceTrue = False
    else:
        voiceTrue = True
    if voiceTrue:
        pass
    return lolvoice

#input
@eel.expose
def ip1fun(ip1lol, page):
    global ip1
    global ip2
    if page == 1:
        ip1 = ip1lol
    elif page == 2:
        ip2 = ip1lol
@eel.expose
def port1fun(port11lol, page):
    global port1
    global port2
    if page == 1:
        port1 = port11lol
    elif page == 2:
        port2 = port11lol
@eel.expose
def login1fun(login1lol, page):
    global login1 
    global login2
    if page == 1:
        login1 = login1lol
    elif page == 2:
        login2 = login1lol
@eel.expose
def password1fun(password1lol, page):
    global password1 
    global password2
    if page == 1:
        password1 = password1lol
    elif page == 2:
        password2 = password1lol
#output
@eel.expose
def outputsetting():
    infooutput = [ip1, port1, login1, password1, ip2, port2, login2, password2]
    return infooutput
@eel.expose
def videoConnect():
    cv(cap)
    if cv(cap) == 0:
        return 0
    else:
        return 1
def printeble():
    print(ip1)

eel.init('main')
eel.start('main.html', size = [1700, 950])