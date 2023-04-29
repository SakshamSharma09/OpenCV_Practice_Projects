import cv2
import datetime
captured = cv2.VideoCapture(0)
print(captured.get(cv2.CAP_PROP_FRAME_WIDTH))
print(captured.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(captured.isOpened()):
    ret, frame = captured.read()

    if ret==True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, 'Saksham', (10, 50), font, 2, (0,255,220), 2, cv2.LINE_AA)
        curr = str(datetime.datetime.now())
        frame = cv2.putText(frame, curr, (10, 200), font, 1, (0, 255, 220), 2, cv2.LINE_AA)
        cv2.imshow('Captured Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

captured.release()
cv2.destroyAllWindows()