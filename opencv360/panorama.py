# -*- coding:utf-8 -*-

import os
import time
import cv2
import imutils
import numpy as np

DIR = './output/final'
R_WIDTH = 8400
WIDTH = 8002
HEIGHT = 4001
BLACK_COLOR = 25
RESULT = './output/result.jpg'
files = os.listdir(DIR)

def stitch(files):
    # stitch files  into panorama
    imgs = []
    for file in files:
        imgs.append(cv2.imread(DIR + '/' + file))
    
    stitcher = cv2.Stitcher.create(mode = 0)
    status,pano = stitcher.stitch(imgs)
    if status == 0:
        return pano
    else:
        return None

def crop(img):
    # cutt of the black borders
    width, height = img.shape[1], img.shape[0]
    if width > R_WIDTH:
        img = imutils.resize(img, width=R_WIDTH)
        width, height = img.shape[1], img.shape[0]

    top, bottom = 0, height
    limit = int(height/8)
    top_limit = limit
    bottom_limit = height - limit

    # top
    c = 0
    while c < width:
        r = 0
        while r < top_limit:
            if sum(img[r,c]) < BLACK_COLOR:
                r = r + 1
            else:
                if r > top:
                    top = r
                break
        c = c + 1
    top = top + 1

    # bottom
    c = 0
    while c < width:
        r = height - 1
        while r > bottom_limit:
            if sum(img[r,c]) < BLACK_COLOR:
                r = r - 1
            else:
                if r < bottom:
                    bottom = r
                break
        c = c + 1
    bottom = bottom -1

    # cut of upper and lower black edges
    tmp = img[top:bottom, 0:width]
    width, height = tmp.shape[1], tmp.shape[0]
    limit = int(height/8)
    left, right = 0, width
    left_limit = limit
    right_limit = width - limit

    # left
    r = 0
    while r < height:
        c = 0
        while c < left_limit:
            if sum(tmp[r,c]) < BLACK_COLOR:
                c = c + 1
            else:
                if c > left:
                    left = c
                break
        r = r + 1

    # right
    r = 0
    while r < height:
        c = width - 1
        while c > right_limit:
            if sum(tmp[r,c]) < BLACK_COLOR:
                c = c - 1
            else:
                if c < right:
                    right = c
                break
        r = r + 1

    # cutt of the left and right black edges
    tmp = tmp[0:height, left:right]
    return tmp

def complement_sky(pano):
    tmp = imutils.resize(pano, width=WIDTH)
    rows, cols = tmp.shape[:2]
    border = HEIGHT - rows

    sky = cv2.imread('sky.jpg')
    sky = imutils.resize(sky, width=WIDTH)
    sky_rows = sky.shape[0]
    start = sky_rows - border
    sky = sky[start:sky_rows]

    # expand to w:h=2:1
    img = np.vstack((sky[:,:], tmp[:,:]))

    mark = np.zeros((HEIGHT, WIDTH), np.uint8)
    color = (0, 0, 0)
    mark[0:border,0:cols] = 255

    # use inpaint
    img = cv2.inpaint(img, mark, 3, cv2.INPAINT_TELEA)

    # blend sky
    tmp_sky = img[0:border,:]
    sky = cv2.addWeighted(tmp_sky, 0.7, sky, 0.3, 0.0)
    img = np.vstack((sky[:,:], img[border:,:]))

    # Gradual in and out fusion of the boundary
    start = border - 1
    end = start - 100
    blend = 0.01
    for r in range(start, end, -1):
        img[r,:] = tmp[0,:] * (1 - blend) + sky[r,:] * blend
        blend = blend + 0.01

    # cut of one pixel on the left and right to avoid black lines
    rows, cols = img.shape[:2]
    img = img[1:,1:cols-1]

    # boundary edge gaussian blur
    tmp = img[0:border+100, :]
    tmp = cv2.GaussianBlur(tmp, (9, 9), 2.5)
    img = np.vstack((tmp[:,:], img[border+100:,:]))

    return img



def PanoramaSIFT():
    start = time.time()

    files = os.listdir(DIR)
    
    pano = stitch(files)
    if pano is not None:
        pano = crop(pano)
        #pano = complement_sky(pano)
        cv2.imwrite(RESULT, pano)
    else:
        print('error')
    end = time.time()
    
    print('cost ' + str(end-start))
    timecost()
    
def timecost(start , end):
    cost = end-start
    return cost
