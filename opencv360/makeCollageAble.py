
import cv2
import numpy as np
import matplotlib.pyplot as plt 
import shutil, random, os

def renameFiles(dir):
    for count, filename in enumerate(os.listdir(dir)):
        dst ="index" + str(count) + ".jpg"
        src =dir+ filename
        dst =dir+ dst
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)


def collageAble(sourceDirectory,destDirectory):
    

    """ if not os.path.exists(destDirectory):
        os.makedirs(destDirectory) """
    
    for imgfile in os.scandir(destDirectory):
        os.remove(imgfile.path)

    filenames = random.sample(os.listdir(sourceDirectory), 6)
    for fname in filenames:
        srcpath = os.path.join(sourceDirectory, fname)
        shutil.copy2(srcpath, destDirectory)
        
    renameFiles(destDirectory)