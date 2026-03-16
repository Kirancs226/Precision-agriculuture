from flask import Flask, render_template, request,redirect, url_for
from services.weather_service import get_weather
from services.crop_service import predict_crop


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        city = request.form["city"]

        # redirect to clean URL
        return redirect(url_for("home", city=city))

    city = request.args.get("city")
    weather = None

    if city:
        weather = get_weather(city)

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





from services.disease_service import predict_disease

from werkzeug.utils import secure_filename
import os

@app.route("/disease", methods=["GET", "POST"])
def disease():

    result = None

    if request.method == "POST":

        file = request.files["image"]

        filename = secure_filename(file.filename)

        upload_folder = "static/uploads"

        path = os.path.join(upload_folder, filename)

        file.save(path)

        result = predict_disease(path)

        print("Prediction:", result)

    return render_template("disease.html", result=result)








if __name__ == "__main__":
    app.run(debug=True)