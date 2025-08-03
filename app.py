from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")
target_names = joblib.load("target_names.pkl")
feature_columns = joblib.load("feature_columns.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            values = [float(request.form[f]) for f in feature_columns]
            prediction = model.predict([values])[0]
            result = target_names[prediction]
        except Exception as e:
            result = "Error: " + str(e)
    return render_template("index.html", result=result, feature_columns=feature_columns)

if __name__ == "__main__":
    app.run(debug=True)
