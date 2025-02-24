from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('complete/<int:pk>/', views.complete_todo, name='complete_todo'),
]