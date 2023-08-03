import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_face = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
cap=cv2.VideoCapture(0)
width=640
height=500

def obj_data(img):
    image_input = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = mp_face.process(image_input)
    if not results.detections:
        print("NO FACE")
    else:    
         for detection in results.detections:
             bbox = detection.location_data.relative_bounding_box
             print(bbox)
             x, y, w, h = int(bbox.xmin*width), int(bbox.ymin * height), int(bbox.width*width),int(bbox.height*height)
             cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
             
            
                
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,500))
    obj_data(frame)
    if cv2.waitKey(1)&0xFF==27:
        break
    cv2.imshow("FRAME",frame)
cap.read()
cv2.destroyAllWindow()
