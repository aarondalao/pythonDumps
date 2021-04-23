import CV2


# enable webcam
# '0' is for the default ID for builtin webcam
# for external webcam ID can be 1 or -1
imcap = cv2.VideoCapture(0)
imcam.set(3, 1280) # set width by 1280
imcap.set(4, 720) # set height by 720


#import cascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    success, img = imcap.read()                                         #capture frame from video

    imgGray = cv2.cvtColor(img, cv2.COLOR_BG2GRAY)                      # converting image from color to grayscale

    # get corners around the face
    # 1.3 = scale factor, 5 = minimun neighbor can be detected

    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)

    # drawing bounding box around face
    for(x,y,w,h) in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)           #  rectangle(img, start point, end point. RGB, thicknesss)

    # displaying image with bounding bx
    #
    cv2.imshow('face_detect', img)

    # keybind 'q' in the keyboard to quit the looping of the face

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    cap.release
    cv2.destroyWindow('face_detect')