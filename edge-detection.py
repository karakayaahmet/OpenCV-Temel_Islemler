import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    edges = cv2.Canny(frame,100,200)

    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()