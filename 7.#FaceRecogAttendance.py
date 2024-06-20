import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)
image_1 = face_recognition.load_image_file("akshay-kumar.jpg")
image_1_encoding = face_recognition.face_encodings(image_1)[0]
image_2 = face_recognition.load_image_file("D:\PythonPrac\salman.jpeg")
image_2_encoding = face_recognition.face_encodings(image_2)[0]

knownface_encodings = [image_1_encoding, image_2_encoding]

knownface_names = ['Akshay', 'Salman']

students = knownface_names.copy()

face_locations = []
face_encodings = []

now = datetime.now()
current_date = now.strftime('%Y-%m-%d')

f = open(f'{current_date}.csv', 'w+', newline='')
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations= face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)
    

    name = None

    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(knownface_encodings, face_encoding)
        
        face_distance = face_recognition.face_distance(knownface_encodings, face_encoding)
        best_match = np.argmin(face_distance)


        if(matches[best_match]):
            name = knownface_names[best_match]
        

        if name in knownface_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomalign = (10, 100)
            fonscale = 1.5
            fontcolor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + "Present", bottomalign, font, fonscale, fontcolor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime('%H-%M-%S')
                lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break        

video_capture.release()
cv2.destroyAllWindows()
f.close()    