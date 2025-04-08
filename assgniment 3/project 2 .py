from flask import Flask, request, jsonify
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

jay_image = face_recognition.load_image_file("faces/jay.jpg")
jay_encoding = face_recognition.face_encodings(jay_image)[0]

khushi_image = face_recognition.load_image_file("faces/khushi.jpg")
khushi_encoding = face_recognition.face_encodings(khushi_image)[0]

virat_image = face_recognition.load_image_file("faces/virat.jpeg")
virat_encoding = face_recognition.face_encodings(virat_image)[0]

jef_image = face_recognition.load_image_file("faces/jef.jpeg")
jef_encoding = face_recognition.face_encodings(jef_image)[0]

prince_image = face_recognition.load_image_file("faces/prince.jpg")
prince_encoding = face_recognition.face_encodings(prince_image)[0]

ary_image = face_recognition.load_image_file("faces/ary.jpg")
ary_encoding = face_recognition.face_encodings(ary_image)[0]

# kaushal_image = face_recognition.load_image_file("faces/kaushal.jpg")
# kaushal_encoding = face_recognition.face_encodings(kaushal_image)[0]


known_face_encodings = [jay_encoding , khushi_encoding , virat_encoding , jef_encoding , prince_encoding , ary_encoding ]
known_face_names = ["jay" , "khushi" , "virat" , "jef" , "prince" , "arqy" ]

student = known_face_names.copy()

face_locations = []
face_encodings = []

now = datetime.now()
currnt_date = now.strftime("%d-%m-%Y")

f=open(f'{currnt_date}.csv','w', newline='')
lnwriter = csv.writer(f)

while True:
    ret, frame = video_capture.read()  # Correctly unpack the frame
    if not ret or frame is None:
        print("Failed to capture frame")
        continue  # Skip processing if frame is not captured

    small_frame = cv2.resize(frame, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)


    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        facce_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(facce_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        if name in known_face_names:
             font = cv2.FONT_HERSHEY_SIMPLEX
             bottomLeftCornerOfText = (10, 100)
             fontScale = 1.5
             fontColor = (0, 0, 0)
             thickness = 3
             linetype = 2
             cv2.putText(frame, name +" present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, linetype)

        if name in student:
            student.remove(name)
            current_time = now.strftime("%H:%M:%S")
            lnwriter.writerow([name, current_time])

    cv2.imshow('attendance', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
