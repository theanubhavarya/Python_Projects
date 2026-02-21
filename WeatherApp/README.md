# 🌦 Weather App – Real-Time Weather with Voice Output

A simple Python-based Weather Application that fetches real-time weather data using WeatherAPI and announces the current temperature using Text-to-Speech.

This project demonstrates API integration, JSON data handling, and voice automation using Python.

---

## 🚀 Features

- Fetches real-time weather data for any city
- Uses WeatherAPI for live data
- Parses JSON response
- Displays full weather response in terminal
- Speaks temperature using Text-to-Speech
- Simple command-line interface

---

## 🛠 Technologies Used

- Python 3
- requests (API integration)
- json (built-in module)
- pyttsx3 (Text-to-Speech engine)

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
4. Extracts the current temperature (in Celsius).
5. Announces the temperature using Text-to-Speech.

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

pip install requests  
pip install pyttsx3  

### 2️⃣ Get Your API Key

- Visit: https://www.weatherapi.com/
- Create a free account
- Generate your API key

### 3️⃣ Insert Your API Key

Open `main.py` and replace:

```
key=YOUR_API_KEY
```

with your actual API key.

⚠ Do NOT upload your real API key to GitHub.

### 4️⃣ Run the Program

```
python main.py
```

---

## 💬 Example

Input:
```
Enter the name of the City: Delhi
```

Output:
- Displays weather JSON data in terminal
- Speaks:
  "The current temperature in Delhi is 28 degree Celsius."

---

## 🔐 Security Note

Do not expose your API key publicly.

If pushing to GitHub:
- Replace your real API key with `YOUR_API_KEY`
- Or store it securely using environment variables

---

## 💡 Future Improvements

- Add humidity and weather condition display
- Add wind speed information
- Add proper error handling for invalid cities
- Convert temperature to Fahrenheit
- Hide API key using environment variables
- Build a GUI version

---

## 👨‍💻 Author

Anubhav Arya  
Python Developer
