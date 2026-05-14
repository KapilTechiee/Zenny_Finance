# from django.urls import path
# from.import views
# Urlpatterns = [
#     path("hello/",views.index,name='zenny'),
# ]     
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name='home'),  # home pageyy
    path("login/", views.login, name='login'),  # login page
    path("trans/",views.trans,name='transactions'),  # transactions page
    path("add/", views.add_transaction, name='add_transaction'),
]
