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
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
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

    is_alone= models.BooleanField(default=False)
    with_parents= models.BooleanField(default=False)
    parents_count=models.IntegerField(null=True, blank=True)
    with_spouse= models.BooleanField(default=False)
    spouse_count= models.IntegerField(null=True, blank=True)
    with_children= models.BooleanField(default=False)
    children_count= models.IntegerField(null=True, blank=True)
    with_siblings= models.BooleanField(default=False)
    siblings_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.full_name
