import cv2
import mediapipe as mp
import cvzone
mp_drawing = mp.solutions.drawing_utils
mp_face = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
cap=cv2.VideoCapture(0)
width=640
height=480


def obj_data(img):
    image_input = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = mp_face.process(image_input)
    if not results.detections:
       print("NO FACE")
    else: 
       for detection in results.detections:
           bbox = detection.location_data.relative_bounding_box
           x, y, w, h = int(bbox.xmin*width), int(bbox.ymin * height), int(bbox.width*width),int(bbox.height*height)
           cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
         

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    obj_width_in_frame=obj_data(frame)
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
