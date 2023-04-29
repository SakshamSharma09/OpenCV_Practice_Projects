import cv2
import numpy as np

def nothing(x):
    pass

#cap = cv2.VideoCapture(0)

cv2.namedWindow("TrackBar")
cv2.createTrackbar("LHue", "TrackBar", 0, 255, nothing)
cv2.createTrackbar("UHue", "TrackBar", 255, 255, nothing)

cv2.createTrackbar("LSaturation", "TrackBar", 0, 255, nothing)
cv2.createTrackbar("USaturation", "TrackBar", 255, 255, nothing)

cv2.createTrackbar("LValue", "TrackBar", 0, 255, nothing)
cv2.createTrackbar("UValue", "TrackBar", 255, 255, nothing)

while True:
    frame = cv2.imread("R.jpeg")
    #ret, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LHue","TrackBar")
    u_h = cv2.getTrackbarPos("UHue","TrackBar")

    l_s = cv2.getTrackbarPos("LSaturation", "TrackBar")
    u_s = cv2.getTrackbarPos("USaturation", "TrackBar")

    l_v = cv2.getTrackbarPos("LValue", "TrackBar")
    u_v = cv2.getTrackbarPos("UValue", "TrackBar")

    l_bound = np.array([l_h, l_s, l_v])
    u_bound = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_bound, u_bound)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Picture", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Res", res)


    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()