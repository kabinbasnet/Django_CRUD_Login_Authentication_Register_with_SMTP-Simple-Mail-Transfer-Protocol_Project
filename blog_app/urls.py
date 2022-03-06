import imp
from unicodedata import name
from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('add/', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('error/', views.error, name='error')
]
