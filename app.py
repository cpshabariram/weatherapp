from flask import Flask, request, render_template
import requests

app = Flask(__name__,template_folder='Templates')

@app.route('/', methods =["GET", "POST"])
def index():
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":
        cityName = request.form.get("cityName")
        if cityName:
            weatherApiKey = 'metion your api key'
            url = "https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=" + we>
            weatherData = requests.get(url).json()
        else:
            error = 1
    return render_template('index.html', data = weatherData, cityName = cityName, error = erro>
if __name__ == "__main__":
        app.debug = True
        app.run()

