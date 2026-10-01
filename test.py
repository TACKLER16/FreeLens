from jarvis import ask_gemini
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
ret, frame = cap.read()
cap.release()
cv2.destroyAllWindows()
result = ask_gemini(frame, "What is this object?")
print(result)
