from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('quiz1', views.quiz1, name = "quiz1"),
    path('quiz2', views.quiz2, name = "quiz2"),
    path('quiz3', views.quiz3, name = "quiz3"),
    path('quiz4', views.quiz4, name = "quiz4"),
]