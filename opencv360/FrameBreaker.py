import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import os, glob

####TO DO                     STATUS
# ~get frames~                done
#count frames                 done
#connecting code to get path  incomplete
#save images function         incomplete
#collage preview              incomplete
#
#generator for reading video

def frameBreaker(VFILE,dir,framesToSkip,frameName,vidName):
    ########clearing previous files in directory###########
    for imgfile in os.scandir(dir):
        os.remove(imgfile.path)
    
#################### Setting up the file ################
    
    vidcap = cv2.VideoCapture(VFILE)
    success, image = vidcap.read()

#################### Setting up parameters ################

#OpenCV is notorious for not being able to good to 
# predict how many frames are in a video. 

   # fps = vidcap.get(cv2.CAP_PROP_FPS)
  
    frame_counter(VFILE)  
    tot_frames = frame_counter.frame_count
    print("total frames in "+vidName+" : %d"  %tot_frames )
  
    n = int(framesToSkip)  
     
                          # Desired interval of frames to include
    desired_frames = np.arange(1,tot_frames , n)
    print(desired_frames) 


#################### Initiate Process ################

    for i in desired_frames:
        vidcap.set(1, i-1)                      
        success, image = vidcap.read(1)         # image is an array of array of [R,G,B] values
        frameId = vidcap.get(1)                # The 0th frame is often a throw-away
        cv2.imwrite(dir + "/"+frameName+"frame%d.jpg" % frameId, image)

    vidcap.release()
    print("Completed" + vidName)
        


def frame_counter(VFILE):
    video = cv2.VideoCapture(VFILE)
    frame_counter.frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video.release()
    



