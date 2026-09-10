from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    city = ''

    if request.method == "POST":
        city = request.form.get('city')

        if city:
            url = f'https://wttr.in/{city}?format=3'

            try: 
                response = requests.get(url, timeout=5)

                if response.status_code == 200:
                   weather_data = response.text
                else:
                     weather_data = "could not fetch weather data."
            except Exception:
                weather_data = 'rror connecting to weather service.'

    return render_template('index.html',
                        weather=weather_data,
                        city=city)
if __name__ == '__main__':
    app.run(debug=True)