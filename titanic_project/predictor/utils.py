# predictor/utils.py
import pandas as pd

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
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    # 1 if alone, 0 if with family)
    df['isAlone'] = 0
    df.loc[df['FamilySize'] == 1, 'isAlone'] = 1

    # Check the first few rows
    print(df[['isAlone', 'FamilySize', 'Survived']].head())

    return df
