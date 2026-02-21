# 🤖 RoboSpeaker – Text to Speech App

RoboSpeaker is a simple Python-based Text-to-Speech (TTS) application that converts user input text into spoken audio using the `pyttsx3` library.

It runs in the terminal and continuously speaks whatever the user types until the user exits.

---

## 🚀 Features

- Converts text to speech in real time
- Continuous input mode
- Simple command-line interface
- Exit option using `q`
- Friendly greeting and exit message

---

## 🛠 Technologies Used

- Python 3
- pyttsx3 (Text-to-Speech library)

---

## 💻 Platform Compatibility

✅ Fully tested and working on **Windows**

⚠ On macOS and Linux:
- May require additional configuration
- Linux users may need to install `espeak`
- Behavior depends on system speech engine support

---

## 📂 Project Structure

RoboSpeaker/
│
├── main.py
└── README.md

---

## ⚙️ How It Works

1. Initializes the `pyttsx3` engine.
2. Continuously takes input from the user.
3. Converts typed text into speech.
4. Speaks the text aloud.
5. If user types `q`, program exits after saying goodbye.

---

## ▶️ How to Run

### 1️⃣ Install Dependency

pip install pyttsx3

### 2️⃣ Run the Program

python main.py

---

## 💻 Example

Welcome to RoboSpeaker 1.1. Created by Anubhav!  
NOTE: Press q to exit.

Enter what you want me to pronounce: Hello  
(RoboSpeaker speaks: Hello)

Enter what you want me to pronounce: q  
(RoboSpeaker speaks: Bye Bye Friend)

---

## 💡 Future Improvements

- Add voice selection (male/female)
- Add speech speed control
- Add volume control
- Add GUI interface
- Add support for saving speech as audio file

---

## 👨‍💻 Author

Anubhav Arya  
Python Developer
