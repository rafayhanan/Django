from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hi/',views.say_Hi),
    path('',views.home,name="home")
]