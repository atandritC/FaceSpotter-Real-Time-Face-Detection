import cv2
import dlib

def detect_faces():
    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = detector(gray)

        i = 0
        for face in faces:
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
            
            i += 1
            
            cv2.putText(frame, 'face num ' + str(i), (x-10, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            print(face, i)
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        yield frame_rgb

    cap.release()