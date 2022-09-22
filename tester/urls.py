from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('list/',views.tasklist),
    path('get/<int:pk>/',views.taskget),
    path('create/',views.taskcreate),
    path('update/<int:pk>/',views.taskupdate),
    path('delete/<int:pk>/',views.taskdelete),

    
]
