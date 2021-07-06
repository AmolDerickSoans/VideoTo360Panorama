
import cv2
import numpy as np
#from PIL import Image


def collageMaker(sourceDirectory,collageNumber):

    

    # read all the images
    # we are going to take 6 images only
    image1=cv2.imread(sourceDirectory+"/index0.jpg")
    image2=cv2.imread(sourceDirectory+"/index1.jpg")
    image3=cv2.imread(sourceDirectory+"/index2.jpg")
    image4=cv2.imread(sourceDirectory+"/index3.jpg")
    image5=cv2.imread(sourceDirectory+"/index4.jpg")
    image6=cv2.imread(sourceDirectory+"/index5.jpg")
    


    # make all the images of same size 
    #so we will use resize function with
    for k in range(6):
        try:

            image1=cv2.resize(image1,(60,60), interpolation = cv2.INTER_AREA)
            image2=cv2.resize(image2,(60,60), interpolation = cv2.INTER_AREA)
            image3=cv2.resize(image3,(60,60), interpolation = cv2.INTER_AREA)
            image4=cv2.resize(image4,(60,60), interpolation = cv2.INTER_AREA)
            image5=cv2.resize(image5,(60,60), interpolation = cv2.INTER_AREA)
            image6=cv2.resize(image6,(60,60), interpolation = cv2.INTER_AREA) 
        except:
            break

    # Now how we will attach image with other image
    # we will create a horizontal stack of images
    # then we will add it to the vertical stack
    # let the horizontal pair be (image1,image2)
    # and (image3,image4)
    # we will use numpy stack function
    Horizontal1=np.hstack([image1,image2,image3])
    Horizontal2=np.hstack([image4,image5,image6])

    # Now the horizontal attachment is done
    # noe vertical attachment
    
    Vertical_attachment=np.vstack([Horizontal1,Horizontal2])
    # Show the final attachment
   
    cv2.imwrite("output/collage%d/FinalCollage.jpg" %collageNumber  ,Vertical_attachment)
    #im = Image.open("output/collage%d/FinalCollage.jpg" %collageNumber)
    #im.save("output/collage%d/FinalCollage.png" %collageNumber)

    
