import logging
import pathlib

import os
import cv2

from opencv360 import estimate_blur
from opencv360 import fix_image_size
from opencv360 import pretty_blur_map


def find_images(image_path,img_extensions=['.jpg', '.png', '.jpeg']):
  
    img_extensions += [i.upper() for i in img_extensions]

    path = pathlib.Path(image_path)
    
      

    if path.is_file():
        
        if path.suffix not in img_extensions:
            logging.info(f'{path.suffix} is not an image extension! skipping {path}')
            
        else:
            print(path)
            yield path


    if path.is_dir():
        
        for img_ext in img_extensions:
            yield from path.rglob(f'*{img_ext}')



def delete_blurred(filePath):
    
    for image_path in find_images(filePath):
        image = cv2.imread(str(image_path))
        if image is None:
            logging.warning(f'warning! failed to read image from {image_path}; skipping!')
            continue

        logging.info(f'processing {image_path}')

       
        blur_map, score, blurry = estimate_blur(image, threshold= 100)
        logging.info(f'image_path: {image_path} score: {score} blurry: {blurry}')

        if blurry == True:
            os.remove(image_path) #access denied? fix your permissions
            print("deleting blurred image " ,image_path)
        else:
            continue 


