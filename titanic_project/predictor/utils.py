# predictor/utils.py
import pandas as pd
import joblib
from predictor.models import PredictionModel
import numpy as np

TITLE_AGE_DEFAULTS = {
    'Mr': 32.3, 'Mrs': 35.9, 'Miss': 21.8, 'Master': 4.5, 'Dr': 42.0
}
GLOBAL_MEAN = 29.7


def preprocess_titanic_data(df):

    # Extract Title
    df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    print(df['Title'].value_counts())

    # Calculate the average age for each title
    title_means = df.groupby('Title')['Age'].transform('mean')
    print(f'title means :{title_means}')

    # Fill missing Age values
    if len(df) > 1:
        df['Age'] = df['Age'].fillna(title_means)
    df['Age'] = df['Age'].fillna(df['Title'].map(TITLE_AGE_DEFAULTS))
    df['Age'] = df['Age'].fillna(GLOBAL_MEAN)

    # Verify
    print(f"Missing ages: {df['Age'].isnull().sum()}")

    # Calculate Family size
    sibsp = df.get('SibSp', 0)
    parch = df.get('Parch', 0)
    df['FamilySize'] = sibsp + parch + 1

    # 1 if alone, 0 if with family)
    df['isAlone'] = 0
    df.loc[df['FamilySize'] == 1, 'isAlone'] = 1

    # Check the first few rows
    print(df[['isAlone', 'FamilySize', 'Survived']].head())

    return df


def predict(data, user):
    model = joblib.load('../ml_models/titanic_model.pkl')

    df = pd.DataFrame({
                'Pclass': int(data.get('travel_class')),
                'Sex': int(data.get('gender')),
                'Age': data.get('age')
            }, index=[0])

    test_df = pd.DataFrame({
                'Pclass': int(data.get('travel_class')),
                'Sex': int(data.get('gender')),
                'Age': data.get('age'),
                'SibSp': 1,
                'Parch': 0,
                'FamilySize': 1,
            }, index=[0])

    probability = model.predict_proba(test_df)
    result = np.argmax(probability)

    PredictionModel.objects.create(
        input_data=user,
        result=result,
        probability=probability)
