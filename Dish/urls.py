from django.urls import path
from . import views

app_name = 'Dish' #  do linkow w html trzeba dodawac ta nazwe

urlpatterns = [
    #widoki posta
    path('', views.home_page, name='home_page'), #pierwszy '' oznacza ze nie pobieramy zadnych argumentow

]