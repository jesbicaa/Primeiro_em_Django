from django.urls import path
from app_cad_users import views

urlpatterns = [
    #rota, view reponsavel, nome da referencia
    #users.com
    path('', views.home, name='home'),
    #users.com/users
    path('users/', views.users, name='listagem_usuarios'),
]
