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

As a model algorithm, we chose the [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).

Every team member tried out one of more models and this model was chosen due to its relatively good performance at 83% accuracy.

### Model Performance

To evaluate the model performance we used three different methods. 

1. Accuracy

The first evaluation was done using scikit-learn's `score()` function, which evaluated the model at 83.80% accuracy. We also used `cross_val_score` and got an average accuracy of 82.27%.

2. Confusion Matrix

Next, we evaluated the model using a confusion matrix.
> [!WARNING]  
> This section needs to be written

3. ROC-AUC

Lastly, we evaluated using ROC-AUC.
> [!WARNING]  
> This section needs to be written

## Overview of the system architecture

