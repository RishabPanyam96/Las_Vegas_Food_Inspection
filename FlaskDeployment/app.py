
from flask import Flask, request, jsonify, render_template, make_response, Response
import numpy as np
import tablib
import pandas as pd
import pickle
import io
import csv
import os

# initialize flask app
app = Flask(__name__)

# load and read the pickle file
model = pickle.load(open('model.pkl', 'rb'))

# csv to html
dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'testingOutput.csv')) as f:
    dataset.csv = f.read()

# Home page
@app.route('/')
def index():
    data = dataset.html
    #return dataset.html
    return render_template('index.html', data=data)


# Login page
@app.route('/login')
def login():
    pass

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

    return render_template('displayResults.html' , data = data)


# Direct API calls through request
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
