from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c3346984e18cb7358c27c387e3a0dfc2'
    path('weather/', views.index1, name="index1"),
    
]
