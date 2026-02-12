# titanic-capstone-project

## Project overview and purpose

This project implements an end-to-end machine learning system built on real-world data and deployed as a web application. It combines data analysis, model development, database design, version control, web development, and agile collaboration into a single, cohesive workflow.

Using historical passenger data from the Titanic disaster, we developed a machine learning model to predict whether a passenger survived. The trained model is integrated into a Django-based web application, allowing users to input passenger details and receive real-time survival predictions.

The primary objective of this project is to simulate a realistic software and machine learning lifecycle. Starting from raw data, we move through data exploration, preprocessing, model training, and evaluation. The system is developed collaboratively using Git and Scrum practices, and concludes with a fully deployed, documented, and user-facing application.

## How to set up and run the project locally

### Cloning from Github

Clone the repository from GitHub using the method of your choice.

### Setting up a virtual environment using Anaconda

> [!NOTE]  
> You can of course create a virtual environment with another method of your choice, e.g. venv or virtualenv. This guide details using Anaconda.

1. Install either [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install) or [Anaconda](https://www.anaconda.com/download) according to the instructions from their website.

2. Open Anaconda Prompt and type `conda create --name <envname> python=3.11`, exchange `envname` with your chosen environment name.

3. Type `conda activate <envname>`, exchange `envname` with your chosen environment name.

### Installing dependencies

1. Navigate to the home directory of the cloned project.
2. Install the dependencies using `pip install -r requirements.txt`

### Running a local Django server

Before you run the server, you need to apply the migrations. First, run `python manage.py makemigrations`, then run `python manage.py migrate`.

To run the server, from the projects home directory, run `python manage.py runserver`

## Description of the machine learning model

For this project, we created a model using the [scikit-learn machine learning library](https://scikit-learn.org/stable/index.html).

### Model Features

The model was trained using the following features:

- Pclass: Passenger class, representing socio-economic status (1 = highest, 3 = lowest)
- Sex
- Age
- SibSp: Number of siblings and/or spouses aboard
- Parch: Number of parents and/or children aboard

FamilySize: Total number of family members traveling together (a value of 1 indicates the passenger was traveling alone)

Some features were used directly from the dataset, while others required preprocessing or feature engineering.

The following features were used directly from the raw data:

- Pclass
- Age
- SibSp
- Parch

Sex was originally a categorical variable and was converted into a numerical representation to make it suitable for model training (male = 0, female = 1).

FamilySize was engineered by combining SibSp and Parch to capture overall family presence aboard the ship. This additional feature helps the model better represent social context beyond individual relationship counts.

If you want, I can also tighten it further or make it more technically detailed (for example, mentioning encoding strategy, scaling, or handling missing values).

### Model Algorithm

As our learning algorithm, we chose the [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) from scikit-learn.

Each team member experimented with one or more candidate models and compared their performance. Based on these evaluations, the RandomForestClassifier was selected due to its strong overall performance, achieving an accuracy of 83% on our validation data.

The final model was trained with the following hyperparameters:

- n_estimators = 100
- max_depth = 5
- random_state = 42

This configuration provided a good balance between predictive performance and model complexity, while keeping the model robust against overfitting.

### Model Performance

To evaluate the model performance we used three different methods.

1. Accuracy

    Accuracy was used as an initial metric to evaluate the overall performance of the model.

    The first evaluation was performed using scikit-learn’s score() function on the test set, resulting in an accuracy of 83.80%. This means that approximately 84% of the passengers in the test data were correctly classified as either survivors or non-survivors.

    To obtain a more robust estimate of the model’s performance, we also applied cross-validation using cross_val_score. This method evaluates the model across multiple train/test splits and averages the results, reducing the risk that the performance estimate is biased by a single split of the data. The mean cross-validation accuracy was 82.27%.

    The relatively small difference between the test accuracy (83.80%) and the cross-validated average (82.27%) indicates that the model performs consistently and does not appear to be significantly overfitting. Overall, the accuracy results confirm that the model provides reliable predictions on unseen data.

2. Confusion Matrix

    To evaluate the performance of the model further, we used a confusion matrix along with standard classification metrics such as precision, recall, and F1-score.

    Confusion matrix (rows: actual, columns: predicted):

    ``` python
    [[95 10]
    [19 55]]
    ```

    This matrix can be interpreted as follows:

    - 95 true negatives: passengers who did not survive and were correctly predicted as non-survivors
    - 55 true positives: passengers who survived and were correctly predicted as survivors
    - 10 false positives: passengers who did not survive but were predicted as survivors
    - 19 false negatives: passengers who survived but were predicted as non-survivors

    Overall, the model achieved an accuracy of 0.84 on the test set (179 samples).

    Class-wise performance:

    - Class 0 (did not survive):

        - Precision: 0.83
        - Recall: 0.90
        - F1-score: 0.87

    - Class 1 (survived):

        - Precision: 0.85
        - Recall: 0.74
        - F1-score: 0.79

    The higher recall for class 0 indicates that the model is particularly strong at correctly identifying non-survivors. However, the lower recall for class 1 shows that some surviving passengers are misclassified as non-survivors.

    The macro and weighted averages (both around 0.83–0.84) indicate balanced overall performance across classes, with no severe class imbalance issues. Overall, the model demonstrates solid predictive capability while still leaving room for improvement, particularly in increasing recall for surviving passengers.

3. ROC-AUC

    In addition to accuracy and the confusion matrix, we evaluated the model using the Receiver Operating Characteristic – Area Under the Curve (ROC–AUC) metric.

    The ROC curve measures the trade-off between the true positive rate (recall) and the false positive rate across different classification thresholds. Instead of evaluating the model at a single fixed threshold (such as 0.5), ROC–AUC assesses how well the model separates the two classes overall.

    Our model achieved an ROC–AUC score of:

    0.8963

    An ROC–AUC score ranges from 0.5 (no discriminative power, equivalent to random guessing) to 1.0 (perfect classification). A value of 0.8963 indicates strong class separability, meaning the model is highly capable of distinguishing between survivors and non-survivors across a wide range of thresholds.

    This relatively high ROC–AUC score confirms that the model’s predictive performance is robust, even beyond the single-threshold accuracy metric, and suggests that it generalizes well to unseen data.

## Overview of the system architecture

The system is implemented as a full-stack Django application that integrates the trained machine learning model directly into the backend. The trained model is serialized and stored as a pickle file, which is loaded by the Django application at runtime. Prediction logic and supporting functionality are encapsulated in helper functions within the app’s utils.py module, keeping the code modular and maintainable.

For data persistence, the project uses SQLite, Django’s default database, which provides a lightweight and straightforward setup suitable for development and deployment in this context.

In addition to the web application, Jupyter notebooks are included in the repository for exploratory data analysis, preprocessing, feature engineering, and visualization. These notebooks document the analytical workflow and model development process, serving as both development artifacts and reproducible documentation of the machine learning pipeline.
