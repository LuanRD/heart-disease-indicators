# Personal Key Indicators of Heart Disease

- 2020 annual CDC survey data of 400k adults related to their health status.
- According to the CDC, heart disease is one of the leading causes of death for people in the US (African Americans, American Indians and Alaska Natives, and white people). About half of all Americans (47%) have at least 1 of 3 key risk factors for heart disease: high blood pressure, high cholesterol, and smoking. Other key indicators include diabetic status, obesity (high BMI), not getting enough physical activity or drinking too much alcohol.
- For more information, you can access the Kaggle Dataset through this [link](https://www.kaggle.com/kamilpytlak/personal-key-indicators-of-heart-disease).

## Objectives
- Make an Exploratory Analysis of each variable showing the prevalence of heart disease for each category; 
- Search for the best combination of hyperparameters for Logistic Regression, SVM, Random Forest, and XGBoost that maximizes the recall avoiding compromising other metrics results as accuracy and specificity;
- Create an API to deploy the best model using Flask and Fast API;
- Create a Web APP with Streamlit with the best model.

## Stacks
- Main Language: Python;
- Model Creation:  Pandas, Matplotlib, Seaborn, Numpy, Sklearn, Imblearn, XGBoost, Skopt, and Yellowbrick;
- Deploy: FastAPI, Flask, HTML, Streamlit (Web app), and Docker.

## Apps (Deployed on Heroku)
- Flask: https://indicators-heart-disease-flask.herokuapp.com/
- Streamlit(english): https://heart-disease-streamlit-lrd.herokuapp.com/
- Streamlit(português): https://indicadores-doencas-cardiacas.herokuapp.com/

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## Exploratory Data Analysis

### Prevalence of heart disease by Age Category
![image](https://user-images.githubusercontent.com/95313119/160165333-eb72669e-9d94-4c02-a77b-9fbcf3fc6ce9.png)

### Prevalence of heart disease by Stroke
![image](https://user-images.githubusercontent.com/95313119/160166757-c72f9035-a3a9-4e8f-9214-8a72488d7ac4.png)


### Prevalence of heart disease by Difficulty of Walk
![image](https://user-images.githubusercontent.com/95313119/160166775-857cb167-36be-4a57-a363-7bda046e76b8.png)


### Prevalence of heart disease by Gender
![image](https://user-images.githubusercontent.com/95313119/160166791-3dc8be9e-5645-4296-86b0-3bd8dac5a9fd.png)


### Prevalence of heart disease by Physical Activity
![image](https://user-images.githubusercontent.com/95313119/160166836-bbbf4cd3-119c-48de-a0ca-15bf553de256.png)


### Prevalence of heart disease by Diabetes
![image](https://user-images.githubusercontent.com/95313119/160166818-8febd2da-6e97-4a57-a908-5fda8f903568.png)


### Prevalence of heart disease by General Health
![image](https://user-images.githubusercontent.com/95313119/160166849-6aed31c4-b587-489f-bbda-0472601bf11b.png)


### Prevalence of heart disease by Kidney Disease
![image](https://user-images.githubusercontent.com/95313119/160166879-1bd59dc1-85b8-4d1b-aeaa-e98fe147ded9.png)


### Prevalence of heart disease by Skin Cancer
![image](https://user-images.githubusercontent.com/95313119/160166900-b435ce90-56dd-4d81-ad91-142d04a68055.png)

## Model Selection

### Area Under the Precision-Recall Curve (AUPRC) of the best model
![image](https://user-images.githubusercontent.com/95313119/161298700-891b3ff1-f1df-4d17-b693-07f4f33bb9e5.png)


### Confusion Matrix of the best model
![image](https://user-images.githubusercontent.com/95313119/161298746-d9481ab9-ce6c-466d-81ae-d0319bd362a8.png)

### Metric Evaluation Results of each model

| Model                             | Recall      | Specificity | Accuracy
| --------------------------------- | ----------- | ----------- | -------- |
| Logistic Regression Under (MCC)   | 0.831781    | 0.689436    | 0.701621 |
| SVC Under (MCC)                   | 0.826849    | 0.690890    | 0.702528 |
| SVC Under (F1)                    | 0.823014    | 0.692531    | 0.703701 |
| Random Forest None (F1)           | 0.820091    | 0.692172    | 0.703701 |
| Random Forest Smote (MCC)         | 0.803836    | 0.699354    | 0.708298 |

## Flask API 

### Interface
![image](https://user-images.githubusercontent.com/95313119/170784972-97af579a-453a-4175-92d6-47d83be5af15.png)
### Result
![image](https://user-images.githubusercontent.com/95313119/170787906-42a70839-f89c-4007-a07c-6e281ee3c61c.png)

## Fast API
![image](https://user-images.githubusercontent.com/95313119/170786821-67b55e95-b2af-407b-9afd-29b7e130b934.png)

## Postman
![image](https://user-images.githubusercontent.com/95313119/170788427-26da98c3-bbb8-4559-a065-1a78e67d8ebf.png)

## Streamlit APP
### Interface
![image](https://user-images.githubusercontent.com/95313119/170787453-89bca058-ce4e-4d2d-bcaa-929b476fdd7a.png)
### Result
![image](https://user-images.githubusercontent.com/95313119/170787578-4e9b98ec-e991-45a0-b859-5813b18aa03d.png)

## Conclusions

- Was made an Exploratory Analysis of each variable showing the prevalence of heart disease for each category. It was shown that have had Stroke, Difficulty to Walk, Kidney Disease and Skin Cancer, aging, and not making Physical Activity are risk factors for someone acquiring heart disease;
-  It was searched for the best combination of hyperparameters for Logistic Regression, SVM, Random Forest, and XGBoost that maximizes the recall avoiding compromising other metrics results as accuracy and specificity. For each method I will be run a parameter tuning for a process without sampling, using Random Undersampler, SMOTE, and both. It will also be tested the use of "f1-macro" and MCC (Mathews Correlation Coefficient) as the evaluation metric for imbalanced data;
- Logistic Regression with Random Undersampling and MCC as the score was defined as the best model, obtaining a recall value of 83,18%, specificity of 68,94%, and accuracy of 70,16%;
- I suggest trying other Classification models, a different Feature Engineering approach to obtain even better results, or setting a different threshold for the best model obtained;
- The model was successfully deployed into a Flask API, FastAPI, and a Web APP was created using Streamlit.
