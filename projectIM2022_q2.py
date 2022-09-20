import cv2
import numpy as np
import skimage
import os


if __name__ == '__main__':
    # check library versions
    libraries = [(cv2,4,5),(np,1,21),(skimage,0,19)]
    for library in libraries:
        version = library[0].__version__.split('.')
        assert library[1] == int(version[0])
        assert library[2] == int(version[1])
        pass
    del libraries

    # load images from folder
    data_folder_location = './images'
    data_folder=os.listdir(data_folder_location)
    del os
    images = []
    for file in data_folder:
        image=cv2.imread(f'{data_folder_location}/{file}')
        images.append(image)

    ## check images
    # for image in images:
    #     cv2.imshow("",image)
    #     cv2.waitKey(0)

