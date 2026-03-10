# Face Recognition Attendance System

A **real-time attendance system** that uses **face recognition** to automatically mark attendance using a webcam. Built with **Python**, **OpenCV**, and the **face_recognition** library.

---

## 🛠 Features

- Detects and recognizes faces in real-time using your webcam.  
- Supports multiple known faces with unique names.  
- Automatically logs attendance in a **CSV file** named with the current date.  
- Draws a rectangle and name over each recognized face.  
- Attendance is marked **only once per person** per session.  
- Press **`q`** to quit the application.

---

## 💻 Technologies Used

- Python 3.13  
- OpenCV (`opencv-python`)  
- face_recognition (`dlib`, `numpy`, `Pillow`)  
- CSV module (built-in)  
- datetime module (built-in)

---

## ⚡ Installation

1. Clone the repository:

# bash
git clone https://github.com/username/face-recognition-attendance.git
cd face-recognition-attendance

# Required Packages

pip install cmake
pip install dlib
pip install face_recognition
pip install opencv-python
pip install numpy
pip install Pillow

# Project Structure

Face_Recognition_Attendance/
│
├── faces/                 # Folder containing known face images
│   ├── ankush.jpg
│   └── modi.jpg
│
├── main.py                # Main Python script
└── README.md

Note: Add the images of people you want to recognize inside the faces/ folder.
      The filename will be used as the display name.

# Run Python file
  python main.py
