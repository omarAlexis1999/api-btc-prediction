from fastapi import FastAPI
import pickle
import statsmodels.tsa.api as smt
import pandas as pd
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "https://react-prediction-graphics.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("./data.csv")
df = df.sort_values(by="date",ascending=True)
df = df.set_index("date")

filename = './model_arima_smt.pkl'
model = pickle.load(open(filename,"rb"))

@app.get("/get-data-historic-btc")
def getDataBtc():
    return df

@app.post("/get-prediction")
def getPrediction(num_times: int):
    return predictionWithModel(num_times)


def predictionLive(numPrediction: int):
    predictions = []
    dates = []

    now = datetime.datetime.strptime(df[-1:].index[0], '%Y-%m-%d %H:%M:%S')
    train = df['Close'].values
    history = [x for x in train]

    for i in range(numPrediction):
        # Config the model
        model = smt.ARIMA(history, order=(0, 2, 0))
        # Train the model
        model_fit_smt = model.fit()
        # Predict with the model
        output = model_fit_smt.forecast()[0]
        predict = output

        # Save the prediction
        predictions.append(predict)
        history.append(output)

        en_una_hora = now + datetime.timedelta(hours=1)
        dates.append(en_una_hora)
        now = en_una_hora

    data = pd.DataFrame(list(zip(predictions, dates)), columns=['Close', "date"])
    data = data.set_index("date")
    return data


def predictionWithModel(numPrediction: int):
    global model
    predictions = []
    dates = []
    ahora = datetime.datetime.strptime(df[-1:].index[0], '%Y-%m-%d %H:%M:%S')

    for i in range(numPrediction):
        new_obs = model.forecast(1)
        modelAux = model.append(new_obs, refit=True)
        model = modelAux

        predictions.append(new_obs[0])
        en_una_hora = ahora + datetime.timedelta(hours=1)
        dates.append(en_una_hora)
        ahora = en_una_hora

    data = pd.DataFrame(list(zip(predictions, dates)), columns=['Close', "date"])
    data = data.set_index("date")
    return data