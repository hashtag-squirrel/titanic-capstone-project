from django.contrib import admin
from predictor.models import UserModel, PredictionModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(PredictionModel)
