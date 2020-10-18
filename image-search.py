import cv2
import numpy as np
import pyautogui


'''

grabs a region (topx, topy, bottomx, bottomy)
to the tuple (topx, topy, width, height)

input : a tuple containing the 4 coordinates of the region to capture

output : a PIL image of the area selected.

'''


def region_grabber(region):    
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1
    return pyautogui.screenshot(region=(x1, y1, width, height))

'''

Searchs for an image within an area

input :

image : path to the image file (see opencv imread for supported types)
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements

returns :
the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not

'''


def imagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None):
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2)) 
        # im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


#Usage 
imagesearcharea("IMAGE_NAME.JPG", 0, 0, 1920, 1080, 0.8) 
