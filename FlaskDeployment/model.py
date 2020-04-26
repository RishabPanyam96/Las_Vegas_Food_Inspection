
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.externals import joblib

# Reading data
dataset = pd.read_csv('*******')

# Creating model and dump as pickle file
# Ex linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model as pickle file
# pickle.dump(regressor, open('model.pkl','wb'))

## Saving model as joblib filename
#joblib.dump(model, "model.joblib", compress = 1) # Compression into 1 filename

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

#print(model.predict([[2, 9, 6]]))
