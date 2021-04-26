# import opencv2 for object detection
import cv2

# remove the comments if you want to use video capture or a photo to detect objects

# FIRST PART : IMAGES
# ADD IMAGES DIRECTLY TO THE PROJECT(INSIDE THE ENV FOLDER) 
# AND CHANGE THE OBJECT INSIDE CV2.IMREAD() "LINE CODE 12 " METHOD WITH YOUR
# DESIRED PHOTO TO BE DETETCTED 

# reads the image
img = cv2.imread('photo.jpg')  
# resize the image 
imgSmall = cv2.resize(img, (600,798))  


# PART 2: USING WEBCAM 

# enable webcam
# '0' is for the default ID for builtin webcam
# for external webcam ID can be 1 or -1
# vidCap = cv2.VideoCapture(1)
# vidCap.set(3, 1280) # set width by 1280
# vidCap.set(4, 720) # set height by 720

# initialise class names 
classNames = []

# select the class file and store it to a variable
classFile = 'coco.names'

# open the file and read it then format the classNames
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
# print(classNames)

# initialise the config path and the weights path

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

# create a model and configure some default settings 

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

# detect the file, set the confidence threshold and attach a bounding box if the predictions is above the certain threshold

classIds, confs, boundingBox = net.detect( imgSmall, confThreshold=0.55)

#print class ids and the bounding box
print(classIds, boundingBox)

# assign new variables for the loop and use zip() to layout the detected objects in the imageSmall
for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), boundingBox):

    # make a rectangle, attach it to the detected object, and set the color to green and thickness to 2
    cv2.rectangle(imgSmall, box, color =(0,255,0), thickness=1)

    # attach text to the bounding box, set the position of the text, and set the font size and font type
    cv2.putText(imgSmall, classNames[classId-1], (box[0] +10, box[1]+ 30), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

# shows the image 
cv2.imshow("output", imgSmall)          
cv2.waitKey(0)