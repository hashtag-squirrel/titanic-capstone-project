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


def calc_sibsp(siblings_count, spouse_count):
    if siblings_count in [None, '']:
        siblings_count = 0
    if spouse_count in [None, '']:
        spouse_count = 0
    sibsp = int(siblings_count) + int(spouse_count)
    return sibsp


def calc_parch(parents_count, children_count):
    if parents_count in [None, '']:
        parents_count = 0
    if children_count in [None, '']:
        children_count = 0
    parch = int(parents_count) + int(children_count)
    return parch


def calc_family_size(sibsp, parch):
    family_size = int(sibsp) + int(parch) + 1
    return family_size


def predict(data, user):
    model = joblib.load('../ml_models/titanic_model.pkl')

    sibsp = calc_sibsp(data.get('siblings_count'), data.get('spouse_count'))
    parch = calc_parch(data.get('parents_count'), data.get('children_count'))
    family_size = calc_family_size(sibsp, parch)

    df = pd.DataFrame({
        'Pclass': int(data.get('travel_class')),
        'Sex': int(data.get('gender')),
        'Age': data.get('age'),
        'SibSp': sibsp,
        'Parch': parch,
        'FamilySize': family_size,
    }, index=[0])

    probability = model.predict_proba(df)
    result = np.argmax(probability)

    survival_probability = round(float(probability[0][1]) * 100, 2)

    PredictionModel.objects.create(
        input_data=user,
        result=result,
        probability=survival_probability)

    return result, survival_probability
