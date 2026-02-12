from django.urls import path
from . import views

app_name = "predictor"

urlpatterns = [
    path("", views.home, name="home"),
    path("userform/", views.userforminfo, name="userforminfo"),
    path("history/", views.HistoryListView.as_view(), name="history-page"),
]
