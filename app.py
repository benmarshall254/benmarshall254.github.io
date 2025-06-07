from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Surebet Prediction App is Live!"
