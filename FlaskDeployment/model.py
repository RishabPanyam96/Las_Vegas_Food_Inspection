
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Reading data
dataset = pd.read_csv('*******')

# Creating model and dump as pickle file
# Ex linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model as pickle file
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

#print(model.predict([[2, 9, 6]]))
