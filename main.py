# pip install cmake 
# pip install face_recognition
# require pip install dlib , numpy , Pillow
# pip install opencv-python
# pip install numpy

import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime

# By default use 0 to get primary web cam
video_capture = cv2.VideoCapture(0)  

# Load known faces & encoding
my_image = face_recognition.load_image_file("faces/ankush.jpg")
my_encoding = face_recognition.face_encodings(my_image)[0]

modi_image = face_recognition.load_image_file("faces/modi.jpg")
modi_encoding = face_recognition.face_encodings(modi_image)[0]

# Store known faces & encoding
known_face_encodings = [my_encoding, modi_encoding]
known_face_names = ["Ankush", "Modi"]

# Make a copy of Students
students = known_face_names.copy()

# Current date and time 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# open file and use current date as a name 
f = open(f"{current_date}.csv", "w", newline="")
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Time"])

# Start loop for camera
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)

        # Using min distance for best mactch
        best_match_index = np.argmin(face_distance)

        name = "Unknown"

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw face rectangle
        top, right, bottom, left = face_location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Mark attendance once
        if name in students:
            students.remove(name)
            current_time = datetime.now().strftime("%H:%M:%S")
            lnwriter.writerow([name, current_time])
            print(f"{name} marked present")

    cv2.imshow("Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release and close file 
video_capture.release()
cv2.destroyAllWindows()
f.close()
