from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "5155a405f99f4f6a335cdf9ac78c629b"

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        print("City entered:", city)
        print("API city:", data["name"])
        print("Main:", data["weather"][0]["main"])
        print("Description:", data["weather"][0]["description"])
        print("--------------------")

        if data.get("cod") == 200:

            temp = data["main"]["temp"]
            condition = data["weather"][0]["main"]
            wind_speed = data["wind"]["speed"]
            if condition == "Clear":
               weather_type = "☀️ Sunny"

            elif condition == "Clouds":
              weather_type = "☁️ Cloudy"

            elif condition in ["Rain", "Drizzle"]:
               weather_type = "🌧️ Rainy"

            elif condition == "Thunderstorm":
                weather_type = "⛈️ Stormy"

            elif condition == "Snow":
               weather_type = "❄️ Snowy"

            elif condition in ["Mist", "Fog", "Haze"]:
              weather_type = "🌫️ Foggy"

            elif wind_speed > 10:
               weather_type = "🌬️ Windy"
            
            else:
               weather_type = "🌤️ Pleasant"
            print("Weather Type:", weather_type)

            if condition == "Rain":
                advice = "☂️ Don't forget your umbrella. Roads may be slippery."

            elif condition == "Thunderstorm":
                advice = "⛈️ Stay indoors if possible and avoid open areas."

            elif condition == "Snow":
                advice = "🧥 It's freezing outside. Wear warm clothes and stay cozy."

            elif temp >= 38:
                advice = "🔥 It's extremely hot today! Wear sunscreen, stay hydrated, and avoid direct sunlight."

            elif temp >= 30:
                advice = "😎 It's quite warm outside. Carry water and wear light clothing."

            elif temp <= 15:
                advice = "🥶 It's chilly today. A sweater or jacket is recommended."

            elif condition == "Clear":
                advice = "☀️ Perfect weather for outdoor activities. Enjoy your day!"

            else:
                advice = "🌤️ The weather looks pleasant today."

            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": weather_type,
                "wind": data["wind"]["speed"],
                "advice": advice
            }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)