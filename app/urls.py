from django.urls import path
from app import views


urlpatterns = [
    path('', views.covid, name='covid'),
    path('covid/', views.covid, name='covid'),
]