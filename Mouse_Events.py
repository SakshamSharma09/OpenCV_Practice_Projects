import numpy as np
import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(image,strXY, (x,y), font, .5, (255,255,0), 2)
        cv2.imshow('Frame', image)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = image[y,x,0]
        green = image[y,x,1]
        red = image[y,x,2];
        font = cv2.FONT_HERSHEY_SIMPLEX
        BGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(image, BGR, (x, y), font, .5, (100, 205, 100), 2)

        cv2.imshow('Frame', image)

image = cv2.imread("E:\Marrriage\ALBUM 01\img02.jpg")
image = cv2.resize(image,(1540,770))
cv2.imshow('Frame', image)

cv2.setMouseCallback('Frame', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()