# Flask Deployment
### Background
Once the final model was created, the last step was to deploy the model. In the workplace, machine learning engineers take the final model provided by the data scientists and deploy it in a production environment. Whether it’s to predict housing sales on a web or mobile app, or real time analysis of click data, certain steps need to be taken to ensure that the model works as intended.
### Application
For our project, the final goal was to add the final model to a web application where a Southern Nevada Health District risk analyst can leverage the model predictions to guide their decision-making
The web application was created using Flask (python web framework), HTML, CSS, and Javascript. A mock login screen was created to ensure that only the risk analysts would be allowed to view the data. In a real production grade environment, where speed is a factor, different, lighter web frameworks would be used instead of Flask.
The final model was saved as a joblib file, which was then used to make the final predictions. For the purposes of showing a quick demo, the prediction results were stored and simply displayed to simulate a real run through. 

### Demo of the web app
![webapp-video](https://media.giphy.com/media/JrGjywp4YRlYYeI58c/giphy.gif)

### Retraining

In a production grade environment, a few things would need to be done differently. Every year, assuming there are new Yelp reviews for the Las Vegas area, the model would be retrained on the new reviews on December 31st. This would be implemented in a batch fashion that would pull data from the Yelp website, spin up an AWS ec2 instance, process the data, train the model, save the results, shut down the ec2 instance, and add it to the website database.

