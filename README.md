# titanic-capstone-project

## Project overview and purpose

In this project, we design and build a complete machine learning system
based on real-world data and deploy it as a web application. The project brings together data analysis, machine learning, database design, version control, web development, and agile teamwork.

We work with historical passenger data from the Titanic disaster to predict whether a passenger survived or not. Using this dataset, our team trained a machine learning model and integrated it into a Django-based web application where users can enter passenger information and receive predictions.

The goal of this project is to simulate a realistic software and machine learning workflow: starting from raw data, moving through analysis and modeling, collaborating via Git and Scrum practices, and ending with a deployed system that is clearly documented and presented.

## How to set up and run the project locally

### Cloning from Github

Clone the repository from GitHub using the method of your choice.

### Setting up a virtual environment using Anaconda

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

## Overview of the system architecture
