# 🎯 Face Recognition Attendance System

A real-time face recognition based attendance system built using Python, OpenCV, and the face_recognition library.

This project captures live video from a webcam, detects faces, compares them with stored known faces, and automatically marks attendance in a CSV file with date and time.

---

## 🚀 Features

- Real-time face detection using webcam
- Face encoding and comparison
- Automatic recognition of known students
- Attendance saved in a CSV file (date-wise)
- Timestamp recording for each recognized student
- Press `Q` to exit

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- face_recognition
- NumPy
- CSV (built-in)
- datetime (built-in)

---

## 📂 Project Structure

FaceRecognitionAttendance/
│
├── faces/
│   ├── anubhav.png
│   ├── shivangi.png
│
├── main.py
└── README.md

---

## ⚙️ How It Works

1. Loads known face images from the `faces/` directory.
2. Encodes facial features using `face_recognition`.
3. Starts webcam feed using OpenCV.
4. Detects and encodes faces in real-time.
5. Compares detected faces with stored encodings.
6. If a match is found:
   - Displays "Name Present" on screen
   - Records attendance in a CSV file with current date and time.

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

pip install opencv-python  
pip install face-recognition  
pip install numpy  

### 2️⃣ Add Known Faces

Place student images inside the `faces/` folder.  
Make sure images are clear and front-facing.

### 3️⃣ Run the Program

python main.py

### 4️⃣ Exit

Press `Q` to stop the program.

---

## 📄 Output

A CSV file will be created with today’s date.

Example:
2026-02-21.csv

Format:
Name, Time

---

## 💡 Future Improvements

- Add GUI interface
- Store attendance in database
- Support multiple images per student
- Add new face registration feature
- Improve recognition accuracy

---

## 👨‍💻 Author

Anubhav Arya  
Python Developer
