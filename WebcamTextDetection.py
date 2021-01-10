import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError ("Камера не обнаружена")
cntr =0;
while True:
    ret,frame = cap.read()
    cntr = cntr+1;
    if ((cntr%0.5)==0):
        imgH, imgW, _ = frame.shape
        x1,y1,w1,h1 = 0,0,imgW,imgH
        imgchar = pytesseract.image_to_string(frame, lang='rus')
        imgboxes = pytesseract.image_to_data(frame, lang='rus')
        for a,b in enumerate(imgboxes.splitlines()):
            if a!=0:
                b = b.split()
                if len(b)==12:
                    x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (50, 50, 255), 2)
                    cv2.putText(frame,b[11],(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

            font = cv2.FONT_HERSHEY_COMPLEX

            cv2.imshow('Results', frame)

            if cv2.waitKey(2) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()