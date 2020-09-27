from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="hp-home"),
    path('about/', views.about, name="hp-about"),
]
