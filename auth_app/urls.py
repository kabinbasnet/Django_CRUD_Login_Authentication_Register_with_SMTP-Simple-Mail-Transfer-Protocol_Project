from django.urls import path
from auth_app import views

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('logout/', views.signout, name='signout')
]
