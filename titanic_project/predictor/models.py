from django.db import models


# Create your models here.
class UserModel(models.Model):
    title_choices = [
       ('mr', 'Mr'),
       ('mrs', 'Mrs'),
       ('master', 'Master'),
       ('miss', 'Miss'),
    ]

    gender_choices = [
        ('0', 'Male'),
        ('1', 'Female'),
    ]

    travel_class_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    ]

    title = models.CharField(max_length=100, choices=title_choices, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=gender_choices,
        blank=True)
    travel_class = models.CharField(
        max_length=10,
        choices=travel_class_choices,
        blank=True)
<<<<<<< HEAD
    port_of_embarkation = models.CharField(
        max_length=10,
        choices=embarkation_choices,
        blank=True)
    is_alone = models.BooleanField(default=False)
    with_parents = models.BooleanField(default=False)
    with_spouse = models.BooleanField(default=False)
    with_children = models.BooleanField(default=False)
    with_siblings = models.BooleanField(default=False)
=======

    is_alone= models.BooleanField(default=False)
    with_parents= models.BooleanField(default=False)
    parents_count=models.BooleanField(default=False)
    with_spouse= models.BooleanField(default=False)
    spouse_count=models.BooleanField(default=False)
    with_children= models.BooleanField(default=False)
    children_count=models.BooleanField(default=False)
    with_siblings= models.BooleanField(default=False)
    sibilings_count=models.BooleanField(default=False)
>>>>>>> origin/main

    def __str__(self):
        return self.full_name


class PredictionModel(models.Model):
    input_data = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    result = models.IntegerField()
    probability = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.input_data.full_name}'
