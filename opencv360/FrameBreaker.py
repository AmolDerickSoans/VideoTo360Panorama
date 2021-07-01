import cv2
import numpy as np 
import matplotlib.pyplot as plt 

####TO DO                     STATUS
# ~get frames~                done
#count frames                 done
#connecting code to get path  incomplete
#save images function         incomplete
#collage preview              done
#
#generator for reading video
def get_frames(filename):
    video = cv2.VideoCapture(filename)
    while video.isOpened():
        ret,frame = video.read()
        if ret:
            yield frame
        else:
            break
    
    video.release()
    yeild None

#retrieve video frames
def get_frame(filename,index):
    counter = 0
    video = cv2.VideoCapture(filename)
    while video.isOpened():
        ret , frame = video.read()
        if ret:
            if counter == index:
                return frame
            counter += 1

        else:
            break
    video.release()
    return None

#get number of frames (requires codec support) so we'll use only mp4 in this case
 
video = cv2.VideoCapture(VFILE)
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
video.release()

 #makes a collage to preview images that where saved

COLLAGE_ROWS = 3
COLLAGE_COLS = 5

collage_num_images = COLLAGE_ROWS * COLLAGE_COLS
skip_frames = frame_count // collage_num_images

frames = []
counter = 0
for f in get_frames(VFILE):
    if counter % skip_frames == 0:
        frames.append(f)
    counter += 1
    
row1 = np.concatenate( frames[0:5], axis=1)
row2 = np.concatenate( frames[5:10], axis=1)
row3 = np.concatenate( frames[10:15], axis=1)
collage = np.concatenate( (row1, row2, row3), axis=0) 
collage = cv2.cvtColor(collage, cv2.COLOR_BGR2RGB)
plt.imshow(collage)

        
