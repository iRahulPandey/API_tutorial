# import libraries
from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource, reqparse
import numpy as np
import pandas as pd
import joblib
import traceback
import pickle

# Your API definition
app = Flask(__name__)
# model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    # return "Hello, Flask!"
    return render_template("index.html")


@app.route("/predict_html", methods=["POST"])
def predict_html():
    if bm:
        try:
            int_features = [int(x) for x in request.form.values()]
            final_features = [np.array(int_features)]
            prediction = list(bm.predict(final_features))
            output = round(prediction[0], 2)

            return render_template(
                "index.html", prediction_text="Prediction {}".format(output)
            )

        except:

            return jsonify({"trace": traceback.format_exc()})
    else:
        print("Train the model first")
        return "No model here to use"


@app.route("/predict", methods=["POST"])
def predict():
    if bm:
        try:
            json_ = request.json
            query = pd.DataFrame(json_)
            prediction = list(bm.predict(query))
            return jsonify({"prediction": str(prediction)})

        except:

            return jsonify({"trace": traceback.format_exc()})
    else:
        print("Train the model first")
        return "No model here to use"


if __name__ == "__main__":

    port = 9696  # If you don't provide any port the port will be set to 12345
    bm = joblib.load("boston_model.joblib")  # Load "boston_model.joblib"
    print("Model loaded")
    # app.run(debug=True)
    app.run(port=port, debug=True, host="0.0.0.0")
