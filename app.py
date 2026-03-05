from flask import Flask, render_template
from services.weather_service import get_weather

app = Flask(__name__)

@app.route("/")
def home():

    weather = get_weather("Chennai")

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)