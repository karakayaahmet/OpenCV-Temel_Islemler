import cv2

cap = cv2.VideoCapture("girit.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False:
        break

    cv2.imshow("video", frame)

    if cv2.waitKey(30) & 0XFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()