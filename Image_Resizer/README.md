# 🖼️ Image Resizer using OpenCV

A simple and efficient image resizing utility built using Python and OpenCV.

This project resizes an image by a configurable percentage and saves the resized output as a new file.

---

## 🚀 Features

- Resize images by percentage
- Preserve original image quality
- Save resized image to a new file
- Simple and beginner-friendly implementation
- Uses OpenCV for fast image processing

---

## 🛠 Technologies Used

- Python 3
- OpenCV (cv2)

---

## 📂 Project Structure

Image_Resizer/
│
├── main.py
├── ImageResizer.py
├── RR.jpg
└── README.md

---

## ⚙️ How It Works

### main.py
- Loads an image using OpenCV
- Calculates new dimensions based on scaling percentage
- Resizes the image
- Saves the resized image to disk

### ImageResizer.py
- Loads an image
- Displays it using OpenCV window
- Waits for a key press before closing

---

## ▶️ How to Run

### 1️⃣ Install Dependency

pip install opencv-python

### 2️⃣ Modify Parameters (Optional)

In `main.py`, you can change:

source = "RR.jpg"  
destination = "RR3.jpeg"  
scale_percent = 50  

### 3️⃣ Run the Script

python main.py

The resized image will be saved as:
RR3.jpeg

---

## 📄 Example

If original image size is:
1920 x 1080

With scale_percent = 50

Output image size will be:
960 x 540

---

## 💡 Future Improvements

- Add custom width & height input
- Add GUI interface
- Batch resize multiple images
- Add aspect ratio lock option
- Convert image formats automatically

---

## 👨‍💻 Author

Anubhav Arya  
Python Developer
