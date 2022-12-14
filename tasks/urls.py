from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deletetask, name="delete"),
    path('index/', views.indexhtml, name="indexhtml"),
    path('about/', views.abouthtml, name="abouthtml")
]

