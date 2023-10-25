from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('completedtodo/', views.completed_todo, name='completedtodo'),
    path('goodbye/', views.goodbye, name='goodbye'),
    path('createtodo/', views.createtodo, name='createtodo'),
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('displaytodo/<int:pk>/', views.display_todo, name='displaytodo'),
    path('todo/delete/<int:pk>/', views.delete_todo, name='deletetodo'),
    path('todo/completedtodo/<int:pk>/', views.delete_todo, name='completedtodo'),
]