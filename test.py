# importing the modules
import cv2
import numpy as np
# read all the images
# we are going to take 4 images only
image1=cv2.imread("index0.jpg")
image2=cv2.imread("index1.jpg")
image3=cv2.imread("index2.jpg")
image4=cv2.imread("index3.jpg")
image5=cv2.imread("index4.jpg")
image6=cv2.imread("index5.jpg")
print("read all files")

# make all the images of same size 
#so we will use resize function
for k in range(6):
        try:

            image1=cv2.resize(image1,(200,200), interpolation = cv2.INTER_AREA)
            image2=cv2.resize(image2,(200,200), interpolation = cv2.INTER_AREA)
            image3=cv2.resize(image3,(200,200), interpolation = cv2.INTER_AREA)
            image4=cv2.resize(image4,(200,200), interpolation = cv2.INTER_AREA)
            image5=cv2.resize(image5,(200,200), interpolation = cv2.INTER_AREA)
            image6=cv2.resize(image6,(200,200), interpolation = cv2.INTER_AREA) 
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
cv2.imshow("Final Collage",Vertical_attachment)
cv2.waitKey(0)
cv2.destroyAllWindows()
