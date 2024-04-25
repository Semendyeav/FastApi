import uvicorn
from fastapi import FastAPI
from check_type import MlModelInput
import pickle
import pandas as pd


#Create the app object
app = FastAPI()
open_model = open("model_car_dataset.pkl", "rb")
ml_model = pickle.load(open_model)
open_encoder = open("encoder_car_dataset.pkl", "rb")
encoder = pickle.load(open_encoder)

#Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'Hello, User'}

#function predict_price need to create a post request to web server
@app.post('/predict')
def predict_price(data: MlModelInput):
    data = data.dict()
    year = data['year']
    mileage = data['mileage']
    brand = data['brand']
    model = data['model']
    color = data['color']
    state = data['state']
    data = {'year': [year], 'mileage': [mileage], 'brand': [brand], 'model': [model],
            'color': [color], 'state': [state]}
    new_df = pd.DataFrame(data)
    en = encoder.transform(new_df.drop(['year', 'mileage'], axis=1))
    df = new_df[['year', 'mileage']].join(en)
    prediction = ml_model.predict(df)[0]
    return {
        'prediction': f"Cost of car is {str(prediction)}$"
    }

#Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
