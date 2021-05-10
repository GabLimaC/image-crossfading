# coding: utf-8
# Author: Gabriel Carvalho de Lima

import argparse
import cv2
import os

#processes argument options for number of images and paths
def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--images", dest="images", default=10,
                        help="Set number of intermediate images to be generated (it has to be an integer greater than 1). By default is set to 10")
    parser.add_argument("-p", "--path", dest="path",
                        help="Manually specify full path to both images", nargs=2)
    options = parser.parse_args()
    return options

#reads image files as vectors using opencv in order to perform operations an manipulate them.
def read_images(imgpath):
    img1 = cv2.imread(imgpath[0], -1)
    img2 = cv2.imread(imgpath[1], -1)
    return ajust_images(img1, img2)

#checks if input for number of images is valid. 
# Additionally, returns True or False depending on the path being specified.
def check_options(n, imgs):
    if n is not None:
        if not n.isdigit():
            raise ValueError("Invalid value for number of images")
        if int(n) <= 1:
            raise ValueError(
                "Invalid number of images, it has to be greater than 1")

    if imgs is not None:
        return True
    return False

#validates path of files provided
def validate (path):
    if len(path) == 2:
        if os.path.exists(path[0]) and os.path.exists(path[1]):
            return
        raise FileNotFoundError("Invalid path for images")
    raise IOError("Program supports 2 files exactly, please check your input directory")

#checks if both images are compatible and if their resolutions match
def ajust_images(img1, img2):
    if not img1.shape[2] == img2.shape[2]:
        raise Exception("Incompatible image formats")
    if not img1.shape == img2.shape:
        #if their resolutions differ, the biggest one will be resized to mach the smaller one
        if img1.shape > img2.shape:
            resized_img = img1
            other_img = img2
        else:
            resized_img = img2
            other_img = img1

        new_shape = other_img.shape[1], other_img.shape[0]
        new_img = cv2.resize(resized_img, new_shape,
                             interpolation=cv2.INTER_AREA)
        return new_img, other_img

    return img1, img2

#this function is responsable for the crossfade itself
def crossfade(i1, i2, n):
    #creating alpha and beta to perform the convex combination
    #alpha and beta are values between 0 and 1, and their sum is always = 1
    #values for alpha and beta are determined by how many intermediate images are required 
    beta = 0
    alpha = 1-beta
    #ratio determins how values for both varibles will change on each loop, and how many loops will be processed
    ratio = 1/(n-1)
    #string used to name each new image file
    img_num = "1"
    for i in range(n):
        #here a new image is generated with current alpha and beta values
        cv2.imwrite("output/image" + img_num + ".jpg", alpha*i1 + beta*i2)
        # prints alpha and beta for each loop
        print("{:4d}° loop: 1st image: {:5.1f}%   |   2nd image: {:5.1f}%".format(i+1, alpha*100, beta*100))
        #updating values for aplha, beta and image number
        img_num = str(int(img_num)+1)
        beta += ratio
        alpha = 1-beta
    return

#main program execution
options = get_options()
if check_options(options.images, options.path):
    path = options.path
else:
    names = os.listdir("input/")
    path = []
    for n in names:
        path.append("input/" + n)

validate(path)
img1, img2 = read_images(path)
num_img = int(options.images)
crossfade(img1, img2, num_img)
