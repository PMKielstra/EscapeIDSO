from tkinter import messagebox

import cv2

WINDOW_TITLE = "QR Scanner"

cap = cv2.VideoCapture(0)
qr_detect = cv2.QRCodeDetector()
qr_data = None

while True:
    ret, img = cap.read()
    cv2.imshow(WINDOW_TITLE, img)
    qr_found, qr_list, _points, _codes = qr_detect.detectAndDecodeMulti(img)
    if qr_found:
        qr_data = qr_list[0]
    key = cv2.waitKey(1)
    if (key == 27  # Escape key
        or cv2.getWindowProperty(WINDOW_TITLE, cv2.WND_PROP_VISIBLE) < 1  # Window closed
        or qr_data is not None): 
        break

cap.release()
cv2.destroyAllWindows()

if qr_data is not None:
    messagebox.showinfo(WINDOW_TITLE, f"QR code found: \"{qr_data}\"")
