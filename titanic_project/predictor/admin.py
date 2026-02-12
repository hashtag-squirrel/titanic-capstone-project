from django.contrib import admin
from predictor.models import UserModel, PredictionModel


@admin.register(PredictionModel)
class PredictionModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('id', 'input_data', 'result', 'probability','created_at')


# Register your models here.
admin.site.register(UserModel)
