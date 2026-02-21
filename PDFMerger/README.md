# 📄 PDF Merger using PyPDF2

A simple Python utility that merges multiple PDF files into a single combined PDF.

This project demonstrates file handling and PDF manipulation using the PyPDF2 library.

---

## 🚀 Features

- Merge multiple PDF files into one
- Lightweight and easy to use
- Uses Python file handling
- Beginner-friendly implementation

---

## 🛠 Technologies Used

- Python 3
- PyPDF2

---

## 📂 Project Structure

PDFMerger/
│
├── 1.pdf
├── 2.pdf
├── sample.pdf
├── merged.pdf
├── main.py
└── README.md

---

## ⚙️ How It Works

1. Creates a list of PDF filenames.
2. Opens each PDF file in read-binary mode.
3. Uses `PyPDF2.PdfReader()` to read each file.
4. Appends each PDF to a `PdfMerger()` object.
5. Writes the combined result into `merged.pdf`.

---

## ▶️ How to Run

### 1️⃣ Install Dependency

pip install PyPDF2

### 2️⃣ Add PDFs

Place all PDFs you want to merge inside the project folder.

Modify this list in `main.py` if needed:

pdfiles = ["1.pdf", "2.pdf", "sample.pdf"]

### 3️⃣ Run the Script

python main.py

---

## 📄 Output

A new file will be created:

merged.pdf

This file contains all PDFs merged in the same order as listed in `pdfiles`.

---

## 💡 Future Improvements

- Take file names as user input
- Add drag-and-drop support
- Add GUI interface
- Allow custom output file name
- Automatically merge all PDFs in folder

---

## 👨‍💻 Author

Anubhav Arya  
Python Developer
