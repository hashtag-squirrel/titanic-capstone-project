from django.db import models

# Create your models here.
class UserModel(models.Model):
    gender_choices=[
       ('male','Male'),
       ('female','Female'),
    ]

    full_name= models.CharField(blank=True)
    age=models.IntegerField(blank=True)
    gender=models.CharField(max_length=10,choices=gender_choices,blank=True)
   

    def __str__(self):
     return self.full_name
