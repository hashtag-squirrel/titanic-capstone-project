from django.db import models


# Create your models here.
class UserModel(models.Model):
    title_choices=[
       ('mr','Mr'),
       ('mrs','Mrs'),
       ('master','Master'),
       ('miss','Miss'),
    ]

    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    travel_class_choices = [
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd')
    ]

    embarkation_choices = [
        ('C', 'Cherbourg'),
        ('Q', 'Queenstown'),
        ('S', 'Southampton')
    ]

    title= models.CharField(max_length=100,choices=title_choices,blank=True)
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
    port_of_embarkation = models.CharField(
        max_length=10,
        choices=embarkation_choices,
        blank=True)
    is_alone= models.BooleanField(default=False)
    with_parents= models.BooleanField(default=False)
    with_spouse= models.BooleanField(default=False)
    with_children= models.BooleanField(default=False)
    with_siblings= models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class PredictionModel(models.Model):
    results = [(1, 'Survived'), (0, 'Deceased')]

    input_data = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    result = models.CharField(max_length=10, choices=results)
    probability = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result
