"""
This script assumes successful installtion of open cv2

"""
import cv2
import sys

#initialize
videoFilePath = sys.argv[0] #absolute path tothe video file
frameStart = sys.argv[1] #start frame of capture
frameEnd = sys.argv[2] #end frame of capture
frameSkip = sys.argv[3] #number of frames to skip between captures
frameName = sys.argv[4] #name of the frame to save in the output jpg capture

vidcap = cv2.VideoCapture(videoFilePath)

#Loop and capture
for i in range(frameStart,frameEnd,frameSkip):
        vidcap.set(0,i)      # cue to required position
        success,image = vidcap.read()
        if success:
                print("Capturing Frame - "+ str(i))
                cv2.imwrite("Cap-" + str(frameName) + "-" + str(i) + ".jpg", image)     # save frame as JPEG file

print("Capture completed. Captured " + str(i) + " frames.")