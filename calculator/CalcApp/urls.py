from django.urls import path
from . import views

urlpatterns = [
    path('', views.App),
    path('about/', views.about),
]

 