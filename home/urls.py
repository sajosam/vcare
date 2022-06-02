from turtle import home
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('main',views.main,name='main'),
    path('search', views.hospital,name="hospital"),
    path('doctor/<int:id>', views.doctor,name="doctor"),
    path('appointment/<int:id>', views.appointment,name="appointment"),
    path('a_confirmation',views.a_confirmation,name='a_confirmation'),


]