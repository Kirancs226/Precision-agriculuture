from flask import Flask, render_template, request
from services.weather_service import get_weather
from services.crop_service import predict_crop

app = Flask(__name__)

@app.route("/")
def home():

    weather = get_weather("Chennai")

    return render_template("index.html", weather=weather)


@app.route("/crop", methods=["GET", "POST"])
def crop():

    result = None

    if request.method == "POST":

        n = float(request.form["nitrogen"])
        p = float(request.form["phosphorus"])
        k = float(request.form["potassium"])
        temp = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        features = [n, p, k, temp, humidity, ph, rainfall]

        result = predict_crop(features)

    return render_template("crop.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)