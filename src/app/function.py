import pickle
import pandas as pd

# pipeline = pickle.load(open('../../models/pipeline.pkl', 'rb'))
pipeline = pickle.load(open('../../models/pipeline.pkl', 'rb'))

columns = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth',
           'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic',
           'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease',
           'SkinCancer']


# Function to transform the inputs and predict if someone has heart disease
def predict_disease(inputs):
    values = []

    for i, j in enumerate(inputs):
        i = []
        i.append(j)
        values.append(i)

    zip_obj = zip(columns, values)
    df = pd.DataFrame(dict(zip_obj))

    prediction = pipeline.predict(df)
    probability = pipeline.predict_proba(df)

    print(f'Probability of having Heart Disease: {(probability[0][1] * 100):.2f}%')

    if prediction[0] == 0:
        print("Result: You probably don't have heart disease.")
    else:
        print("You probably have heart disease.")


new_inputs = [20.7, 'No', 'No', 'No', 4, 30, 'No', 'Female', '18-24', 'White', 'No', 'No', 'Fair', 7, 'No', 'No', 'No']
predict_disease(new_inputs)
