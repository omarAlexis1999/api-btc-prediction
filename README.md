# api-btc-prediction
The api has calls that consume a machine learning model trained with the Python statsmodels library for time series forecasting.
To predict the price of the Bitcoin cryptocurrency in a period of hours.

The app is implemented in Heroku in the following resource https://api-btc-prediction.herokuapp.com/docs.

As an example of api consumption implementation is the following project: https://github.com/omarAlexis1999/fronted-btc-prediction-.git

## Instalation

**`git clone https://github.com/omarAlexis1999/api-btc-prediction.git`**

Then enter the created folder.

**`cd api-btc-prediction`**

To install project dependencies use the following command.


**`pip install -r requirements.txt`**

To run the API in your local environment use the following command

**`uvicorn predictionApi:app --reload`**

This will run the application on port 8000 on localhost 127.0.0.1.

**http://127.0.0.1:8000/docs**

![image](https://user-images.githubusercontent.com/52268702/155027679-cd12d41f-dd06-4ef6-b5ce-7c4f0888e8b4.png)

## Authors by

Project Created by **Omar Sanmartin and Johanna P. Montaño**
