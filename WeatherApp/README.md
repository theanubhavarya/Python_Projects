# 🌦 Weather App – Real-Time Weather with Voice Output

A Python-based Weather Application that fetches real-time weather data using an external API and speaks the temperature aloud using Text-to-Speech.

This project demonstrates API integration, JSON parsing, and voice automation.

---

## 🚀 Features

- Fetches real-time weather data
- Uses external Weather API
- Parses JSON response
- Displays full weather response
- Speaks temperature using Text-to-Speech
- Simple command-line interface

---

## 🛠 Technologies Used

- Python 3
- requests (API calls)
- json (built-in)
- pyttsx3 (Text-to-Speech)

---

## 💻 Platform Compatibility

✅ Fully tested on **Windows**

⚠ On macOS/Linux:
- `pyttsx3` may require additional configuration
- Linux users may need to install `espeak`

---

## 📂 Project Structure

WeatherApp/
│
├── main.py
└── README.md

---

## ⚙️ How It Works

1. Takes city name as input from user.
2. Sends a GET request to WeatherAPI.
3. Receives weather data in JSON format.
4. Extracts current temperature.
5. Speaks the temperature aloud using `pyttsx3`.

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

pip install requests  
pip install pyttsx3  

### 2️⃣ Get Your Own API Key (Recommended)

- Visit: https://www.weatherapi.com/
- Create a free account
- Generate your API key
- Replace the key inside:

url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"

### 3️⃣ Run the Program

python main.py

---

## 💬 Example

Enter the name of the City: Delhi  

Output:
- Displays JSON weather data
- Speaks:
  "The current temperature in Delhi is 28 degree Celsius."

---

## 🔐 Important Note

⚠ Do NOT expose your personal API key publicly.

For security:
- Store API key in environment variables
- Or use a config file

---

## 💡 Future Improvements

- Add weather condition (rainy, cloudy, etc.)
- Add humidity & wind speed
- Add error handling for invalid city names
- Add GUI interface
- Hide API key using environment variables
- Support Fahrenheit conversion

---

## 👨‍💻 Author

Anubhav Arya  
Python Developer
