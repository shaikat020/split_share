# tracker/urls.py
from django.urls import path
from . import views

app_name = 'expense_tracker'

urlpatterns = [
    path('', views.index, name='index'),
]
