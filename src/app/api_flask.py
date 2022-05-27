import pickle
from flask import Flask, request, render_template, make_response
import pandas as pd

app = Flask(__name__, static_url_path='/static')
pipeline = pickle.load(open('../../models/pipeline.pkl', 'rb'))

columns = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth',
           'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic',
           'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease',
           'SkinCancer']


@app.route('/')
def display():
    return 'Heart Disease Prediction'


@app.route('/prediction/', methods=['POST'])
def prediction():
    data = request.get_json()
    inputs = list(data.values())
    values = []

    for i, j in enumerate(inputs):
        i = []
        i.append(j)
        values.append(i)

    zip_obj = zip(columns, values)
    df = pd.DataFrame(dict(zip_obj))

    prediction = pipeline.predict(df)
    probability = pipeline.predict_proba(df)

    if prediction[0] == 0:
        return f'Result: You probably do not have heart disease. Probability = {(probability[0][1] * 100):.2f}%'
    else:
        return f'Result: You probably have heart disease. Probability = {(probability[0][1] * 100):.2f}%'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
