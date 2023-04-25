from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"), # name="routes" is used in studybuddy\base\api\urls.py
    path('rooms/', views.get_rooms, name="rooms"),
]