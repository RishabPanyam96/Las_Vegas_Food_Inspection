
from flask import Flask, request, jsonify, render_template, make_response, Response, url_for
import numpy as np
import tablib
import pandas as pd
import pickle
import io
import csv
import os
from sklearn.externals import joblib


# Initialize flask app
app = Flask(__name__)


# load and read the pickle file
model = pickle.load(open('model.pkl', 'rb'))

# Loading the joblib file
# model = joblib.load('model.joblib')

# csv to html
dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'testingOutput.csv')) as f:
    dataset.csv = f.read()



# Login page
@app.route('/', methods=["GET", "POST"])
def login():
    data = dataset.html
    if request.method == "GET":
        return render_template("login.html", loginfail = False)
    else:
        username = request.form["username"]
        password = request.form["password"]

        if username == 'admin' and password == 'password':
            success = True
        else:
            success = False

        if not success:
            return render_template("login.html", loginfail = True, data = data)
        else:
            # Set cookie for admin to true
            return render_template("index.html", loginfail = False)



# Download the csv
@app.route('/getCSV')
def getPlotCSV():
    with open("testingOutput.csv") as fp:
        csv = fp.read()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})



# Predict button
@app.route('/predict', methods=['GET'])
def predict():
    data = dataset.html
    # Making the prediction based on the most recent model
    #prediction = model.predict(final_features)


    # Placeholder for output
    #output = round(prediction[0], 2)
    # prediction_text='Employee Salary should be $ {}'.format(output)

    return render_template('displayResults.html', data = data)


# Direct API calls through request
@app.route('/predict_api', methods=['POST'])
def predict_api():
    pass

if __name__ == "__main__":
    app.run(debug=True)
