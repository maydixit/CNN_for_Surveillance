"""
This script assumes successful installtion of open cv2

"""
import cv2
import sys

#initialize
videoFilePath = sys.argv[1] #absolute path tothe video file
frameStart = long(sys.argv[2]) #start time of frame of capture (in MS)
frameEnd = long(sys.argv[3]) #end time of frame of capture (in MS)
frameSkip = long(sys.argv[4]) #number of frames to skip between captures
frameName = sys.argv[5] #name of the frame to save in the output jpg capture
augment = sys.argv[6] # 0 = off and 1 = on (augment the frames)

vidcap = cv2.VideoCapture(videoFilePath)

#Loop and capture
for i in range(frameStart, frameEnd, frameSkip):
        vidcap.set(0,i)      # cue to required position
        success,image = vidcap.read()
        if success:
                print("Capturing Frame - "+ str(i))                                
                if augment == "1":
                	vertFlip = cv2.flip(image,1)
                        # save frame as JPEG file
                        cv2.imwrite("Cap-FlippedVert-" + str(frameName) + "-" + str(i) + ".jpg", vertFlip)
                	horizFlip = cv2.flip(image,0)
                        # save frame as JPEG file
                        cv2.imwrite("Cap-FlippedHoriz-" + str(frameName) + "-" + str(i) + ".jpg", horizFlip)
                	grayScale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)                	
                        # save frame as JPEG file
                        cv2.imwrite("Cap-Grayscale-" + str(frameName) + "-" + str(i) + ".jpg", grayScale)
                        #original image
                        cv2.imwrite("Cap-" + str(frameName) + "-" + str(i) + ".jpg", image)     # save frame as JPEG file
                else:
                        print("other")
                        cv2.imwrite("Cap-" + str(frameName) + "-" + str(i) + ".jpg", image)     # save frame as JPEG file


print("Capture completed. Captured " + str(i) + " frames.")