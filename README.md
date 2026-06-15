# weather-detection
WeatherScape

WeatherScape is a web application developed using Flask that provides real-time weather information for cities around the world. The application retrieves weather data from the OpenWeather API and presents it through a clean and user-friendly interface.

Features

- Search weather information by city name
- Display current temperature
- Display humidity level
- Display wind speed
- Identify weather conditions such as Clear, Cloudy, Rainy, Stormy, and Foggy
- Provide weather-based recommendations and advice
- Live clock and time-based greeting
- Error handling for invalid city names
- Responsive and visually appealing user interface

Technologies Used

Backend

- Python
- Flask
- Requests Library

Frontend

- HTML
- CSS
- JavaScript

API

- OpenWeather API

Project Structure

weatherscape/
│
├── app.py
├── requirements.txt
├── .gitignore
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── index.html

Installation and Setup

Step 1: Clone the Repository

git clone <repository-url>

Step 2: Navigate to the Project Directory

cd weatherscape

Step 3: Create a Virtual Environment

python -m venv venv

Step 4: Activate the Virtual Environment

Windows:

venv\Scripts\activate

Step 5: Install Required Packages

pip install -r requirements.txt

Step 6: Obtain an OpenWeather API Key

1. Create an account on OpenWeather.
2. Generate an API key.
3. Open "app.py".
4. Replace the placeholder value with your API key:

API_KEY = "YOUR_API_KEY"

Step 7: Run the Application

python app.py

Step 8: Open the Application

Open a web browser and visit:

http://127.0.0.1:5000

Application Workflow

1. The user enters a city name.
2. The application sends a request to the OpenWeather API.
3. Weather data is retrieved and processed.
4. Weather details are displayed to the user.
5. Weather-specific advice is generated based on the current conditions.
6. Invalid city names are handled with an appropriate error message.

Future Enhancements

- Current location weather using geolocation
- Sunrise and sunset information
- Feels-like temperature
- Visibility information
- Dynamic weather backgrounds and animations
- Dark mode support
- Extended weather forecasts

Author

WeatherScape was developed as a Flask-based web application project to demonstrate API integration, backend development, frontend design, and user interaction using modern web technologies.