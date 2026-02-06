from django.db import models

# Create your models here.
class UserModel(models.Model):
    gender_choices=[
       ('male','Male'),
       ('female','Female'),
    ]

    travel_class_choices=[
       ('1','1st'),
       ('2','2nd'),
       ('3','3rd')
    ]

    embarkation_choices=[
       ('C','Cherbourg'),
       ('Q','Queenstown'),
       ('S','Southampton')
    ]

    full_name= models.CharField(max_length=100,blank=True)
    age=models.IntegerField(blank=True,null=True)
    gender=models.CharField(max_length=10,choices=gender_choices,blank=True)
    travel_class=models.CharField(max_length=10,choices=travel_class_choices,blank=True)
    port_of_embarkation=models.CharField(max_length=10,choices=embarkation_choices,blank=True)
    cabin=models.CharField(max_length=100,blank=True)
   

    def __str__(self):
     return self.full_name
